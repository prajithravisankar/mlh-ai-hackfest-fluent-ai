import json
import logging
import uuid

from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Optional

from database import get_db
from elevenlabs_config.personas import PERSONAS, build_system_prompt

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/lessons", tags=["lessons"])


class StartLessonRequest(BaseModel):
    user_id: str = "user_1"
    title: str = "Conversation Practice"
    objectives: list[str] = ["Improve overall fluency"]
    character: str = "coach_alex"
    target_vocabulary: list[str] = []
    target_idioms: list[str] = []
    pressure_mode: bool = False


class EndLessonRequest(BaseModel):
    user_id: str = "user_1"


@router.post("/start")
async def start_lesson(body: StartLessonRequest, request: Request):
    """Create a new lesson session, initialize orchestrator, return lesson config."""
    lesson_id = str(uuid.uuid4())[:8]

    # Store lesson in DB
    async with get_db() as db:
        await db.execute(
            """INSERT INTO lessons (id, user_id, title, character, status, objectives)
               VALUES (?, ?, ?, ?, 'active', ?)""",
            (lesson_id, body.user_id, body.title, body.character, json.dumps(body.objectives)),
        )
        await db.commit()

    # Build the system prompt for ElevenLabs
    # Fetch user's Speech DNA for personalization
    speech_dna = None
    async with get_db() as db:
        row = await db.execute_fetchall(
            """SELECT * FROM speech_dna_snapshots WHERE user_id = ?
               ORDER BY created_at DESC LIMIT 1""",
            (body.user_id,),
        )
        if row:
            r = row[0]
            speech_dna = {
                "grammar": r["grammar"],
                "vocabulary": r["vocabulary"],
                "filler_words": r["filler_words"],
                "sentence_complexity": r["sentence_complexity"],
                "idiom_usage": r["idiom_usage"],
                "speaking_pace": r["speaking_pace"],
                "coherence": r["coherence"],
                "confidence": r["confidence"],
            }

    system_prompt = build_system_prompt(
        character=body.character,
        objectives=body.objectives,
        target_vocabulary=body.target_vocabulary,
        target_idioms=body.target_idioms,
        speech_dna=speech_dna,
        pressure_mode=body.pressure_mode,
    )

    persona = PERSONAS.get(body.character, PERSONAS["coach_alex"])

    logger.info(f"Lesson started: id={lesson_id}, character={body.character}, pressure={body.pressure_mode}")

    return {
        "lesson_id": lesson_id,
        "title": body.title,
        "character": {
            "name": persona["name"],
            "role": persona.get("role", "English Coach"),
            "style": persona["style"],
            "avatar": persona.get("avatar", "🎤"),
        },
        "objectives": body.objectives,
        "system_prompt": system_prompt,
        "pressure_mode": body.pressure_mode,
    }


@router.post("/{lesson_id}/end")
async def end_lesson(lesson_id: str, request: Request):
    """End a lesson session, save DNA snapshot, update DB status."""
    orchestrator = request.app.state.orchestrator

    # Update lesson status in DB
    async with get_db() as db:
        await db.execute(
            "UPDATE lessons SET status = 'completed', ended_at = datetime('now') WHERE id = ?",
            (lesson_id,),
        )
        await db.commit()

    # Save final DNA snapshot
    dna_agent = orchestrator.get_agent("dna")
    if dna_agent:
        dna = dna_agent.get_current_dna(lesson_id)
        if any(v > 0 for v in dna.values()):
            try:
                async with get_db() as db:
                    # Look up user_id from lesson
                    row = await db.execute_fetchall(
                        "SELECT user_id FROM lessons WHERE id = ?", (lesson_id,)
                    )
                    user_id = row[0]["user_id"] if row else "user_1"

                    await db.execute(
                        """INSERT INTO speech_dna_snapshots
                           (user_id, grammar, vocabulary, filler_words,
                            sentence_complexity, idiom_usage, speaking_pace, coherence, confidence)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (
                            user_id,
                            dna.get("grammar", 0),
                            dna.get("vocabulary", 0),
                            dna.get("filler_words", 0),
                            dna.get("sentence_complexity", 0),
                            dna.get("idiom_usage", 0),
                            dna.get("speaking_pace", 0),
                            dna.get("coherence", 0),
                            dna.get("confidence", 0),
                        ),
                    )
                    await db.commit()
            except Exception as e:
                logger.error(f"Failed to save DNA snapshot: {e}")

        dna_agent.clear_session(lesson_id)

    # Clean up other agent sessions
    for agent_name in ("analyzer", "coach"):
        agent = orchestrator.get_agent(agent_name)
        if agent:
            agent.clear_session(lesson_id)

    # Broadcast lesson end via WebSocket
    ws_manager = getattr(request.app.state, "ws_manager", None)
    if ws_manager:
        await ws_manager.broadcast(lesson_id, {
            "type": "lesson_end",
            "data": {"lesson_id": lesson_id},
        })

    logger.info(f"Lesson ended: id={lesson_id}")
    return {"lesson_id": lesson_id, "status": "completed"}


@router.get("/{lesson_id}")
async def get_lesson(lesson_id: str):
    """Return lesson data + analysis history."""
    async with get_db() as db:
        # Get lesson record
        rows = await db.execute_fetchall(
            "SELECT * FROM lessons WHERE id = ?", (lesson_id,)
        )
        if not rows:
            return {"error": "Lesson not found"}
        lesson = dict(rows[0])
        lesson["objectives"] = json.loads(lesson.get("objectives", "[]"))

        # Get all analysis chunks
        analyses = await db.execute_fetchall(
            """SELECT grammar_score, vocabulary_score, filler_count,
                      sentence_complexity_score, idiom_score, pace_wpm,
                      coherence_score, confidence_score, mistakes,
                      missed_opportunities, created_at
               FROM lesson_analyses WHERE lesson_id = ?
               ORDER BY created_at ASC""",
            (lesson_id,),
        )
        lesson["analyses"] = [
            {
                **dict(a),
                "mistakes": json.loads(a["mistakes"] or "[]"),
                "missed_opportunities": json.loads(a["missed_opportunities"] or "[]"),
            }
            for a in analyses
        ]

    return lesson
