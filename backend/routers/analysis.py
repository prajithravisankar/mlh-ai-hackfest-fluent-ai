import json
import logging
from typing import Optional

from fastapi import APIRouter, Request
from pydantic import BaseModel

from database import get_db

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["analysis"])


# ---- Pydantic models for tool call requests ----

class AnalyzeSpeechRequest(BaseModel):
    transcript: str
    lesson_id: Optional[str] = None


class GetLessonContextRequest(BaseModel):
    lesson_id: Optional[str] = None


class EndLessonRequest(BaseModel):
    final_transcript: str
    lesson_id: Optional[str] = None


# ---- ElevenLabs tool call endpoints ----

@router.post("/tools/analyze_speech")
async def analyze_speech(body: AnalyzeSpeechRequest, request: Request):
    """Called by ElevenLabs agent tool call to analyze a transcript chunk via Gemini."""
    orchestrator = request.app.state.orchestrator

    # Dispatch transcript_chunk event → AnalyzerAgent runs Gemini analysis
    # and publishes analysis_result → CoachAgent + DNAAgent react
    results = await orchestrator.dispatch("transcript_chunk", {
        "transcript": body.transcript,
        "lesson_id": body.lesson_id or "unknown",
    })

    # Extract analysis from AnalyzerAgent's result
    analysis = None
    for r in results:
        if r["agent"] == "analyzer" and r["data"]:
            analysis = r["data"]
            break

    if not analysis:
        logger.warning("AnalyzerAgent returned no analysis — using fallback")
        from services.gemini_analyzer import FALLBACK_ANALYSIS
        analysis = dict(FALLBACK_ANALYSIS)

    # Store analysis in database
    lesson_id = body.lesson_id or "unknown"
    try:
        async with get_db() as db:
            await db.execute(
                """INSERT INTO lesson_analyses
                   (lesson_id, grammar_score, vocabulary_score, filler_count,
                    sentence_complexity_score, idiom_score, pace_wpm,
                    coherence_score, confidence_score, mistakes, missed_opportunities)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    lesson_id,
                    analysis["grammar_score"],
                    analysis["vocabulary_score"],
                    analysis["filler_count"],
                    analysis["sentence_complexity_score"],
                    analysis["idiom_score"],
                    analysis["pace_wpm"],
                    analysis["coherence_score"],
                    analysis["confidence_score"],
                    json.dumps(analysis.get("mistakes", [])),
                    json.dumps(analysis.get("missed_opportunities", [])),
                ),
            )
            await db.commit()
    except Exception as e:
        logger.error(f"Failed to store analysis: {e}")

    # Broadcast analysis via WebSocket
    ws_manager = getattr(request.app.state, "ws_manager", None)
    if ws_manager and body.lesson_id:
        await ws_manager.broadcast(body.lesson_id, {
            "type": "analysis_result",
            "data": analysis,
        })

    # Also check for difficulty adjustments from CoachAgent
    difficulty_adj = None
    for r in results:
        if r["agent"] == "coach" and r["data"] and r["data"].get("difficulty_adjustment"):
            difficulty_adj = r["data"]
            break

    # Include coaching guidance in response to ElevenLabs (so AI adapts)
    response = dict(analysis)
    if difficulty_adj:
        response["coaching_directive"] = {
            "adjustment": difficulty_adj["difficulty_adjustment"],
            "reason": difficulty_adj["reason"],
            "recurring_errors": difficulty_adj.get("recurring_errors", []),
        }
        # Broadcast difficulty adjustment
        if ws_manager and body.lesson_id:
            await ws_manager.broadcast(body.lesson_id, {
                "type": "difficulty_adj",
                "data": difficulty_adj,
            })

    logger.info(
        f"analyze_speech: lesson={lesson_id}, grammar={analysis['grammar_score']}, "
        f"vocab={analysis['vocabulary_score']}, fillers={analysis['filler_count']}"
    )
    return response


@router.post("/tools/get_lesson_context")
async def get_lesson_context(body: GetLessonContextRequest):
    """Called by ElevenLabs agent to get current lesson objectives."""
    lesson_id = body.lesson_id or "diagnostic"

    # Try fetching real lesson data from DB
    try:
        async with get_db() as db:
            rows = await db.execute_fetchall(
                "SELECT * FROM lessons WHERE id = ?", (lesson_id,)
            )
            if rows:
                lesson = rows[0]
                return {
                    "lesson_id": lesson_id,
                    "title": lesson["title"],
                    "objectives": json.loads(lesson["objectives"] or "[]"),
                    "character": lesson["character"],
                    "target_vocabulary": [],
                    "target_idioms": [],
                }
    except Exception as e:
        logger.error(f"Failed to fetch lesson context: {e}")

    # Fallback for diagnostic or unknown lessons
    return {
        "lesson_id": lesson_id,
        "title": "Diagnostic Conversation",
        "objectives": [
            "Assess baseline fluency",
            "Evaluate grammar accuracy",
            "Measure vocabulary depth",
            "Count filler word usage",
            "Gauge confidence level",
        ],
        "character": "coach_alex",
        "target_vocabulary": ["articulate", "elaborate", "perspective", "implement", "collaborate"],
        "target_idioms": ["hit the ground running", "the bottom line", "think outside the box"],
    }


@router.post("/tools/end_lesson")
async def end_lesson_tool(body: EndLessonRequest, request: Request):
    """Called by ElevenLabs agent when the lesson ends."""
    orchestrator = request.app.state.orchestrator
    lesson_id = body.lesson_id or "unknown"

    # Publish lesson_end event
    await orchestrator.dispatch("lesson_end", {
        "final_transcript": body.final_transcript,
        "lesson_id": lesson_id,
    })

    # Save final DNA snapshot to database
    dna_agent = orchestrator.get_agent("dna")
    if dna_agent:
        dna = dna_agent.get_current_dna(lesson_id)
        try:
            async with get_db() as db:
                await db.execute(
                    """INSERT INTO speech_dna_snapshots
                       (user_id, grammar, vocabulary, filler_words,
                        sentence_complexity, idiom_usage, speaking_pace, coherence, confidence)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        "user_1",  # TODO: real user from auth
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

        # Clean up agent session data
        dna_agent.clear_session(lesson_id)

    # Clean up other agents
    analyzer_agent = orchestrator.get_agent("analyzer")
    if analyzer_agent:
        analyzer_agent.clear_session(lesson_id)

    coach_agent = orchestrator.get_agent("coach")
    if coach_agent:
        coach_agent.clear_session(lesson_id)

    # Broadcast lesson end via WebSocket
    ws_manager = getattr(request.app.state, "ws_manager", None)
    if ws_manager and body.lesson_id:
        await ws_manager.broadcast(body.lesson_id, {
            "type": "lesson_end",
            "data": {"lesson_id": body.lesson_id},
        })

    logger.info(f"end_lesson called for lesson={lesson_id}, transcript_len={len(body.final_transcript)}")
    return {"status": "lesson_ended", "lesson_id": lesson_id}


# ---- Existing analysis endpoints ----

@router.get("/analysis/{lesson_id}")
async def get_analysis(lesson_id: str):
    """Return all analysis chunks stored for a lesson."""
    try:
        async with get_db() as db:
            cursor = await db.execute(
                "SELECT * FROM lesson_analyses WHERE lesson_id = ? ORDER BY created_at",
                (lesson_id,),
            )
            rows = await cursor.fetchall()
            analyses = []
            for row in rows:
                analyses.append({
                    "id": row["id"],
                    "lesson_id": row["lesson_id"],
                    "grammar_score": row["grammar_score"],
                    "vocabulary_score": row["vocabulary_score"],
                    "filler_count": row["filler_count"],
                    "sentence_complexity_score": row["sentence_complexity_score"],
                    "idiom_score": row["idiom_score"],
                    "pace_wpm": row["pace_wpm"],
                    "coherence_score": row["coherence_score"],
                    "confidence_score": row["confidence_score"],
                    "mistakes": json.loads(row["mistakes"]) if row["mistakes"] else [],
                    "missed_opportunities": json.loads(row["missed_opportunities"]) if row["missed_opportunities"] else [],
                    "created_at": row["created_at"],
                })
            return {"lesson_id": lesson_id, "analyses": analyses, "count": len(analyses)}
    except Exception as e:
        logger.error(f"Failed to fetch analyses: {e}")
        return {"lesson_id": lesson_id, "analyses": [], "count": 0}


@router.get("/analysis/{lesson_id}/report")
async def get_report(lesson_id: str):
    # TODO: implement in P05
    return {"lesson_id": lesson_id, "report": {}}
