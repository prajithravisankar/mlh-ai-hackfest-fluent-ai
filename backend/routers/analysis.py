import logging
from typing import Optional

from fastapi import APIRouter, Request
from pydantic import BaseModel

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
    """Called by ElevenLabs agent tool call to analyze a transcript chunk."""
    orchestrator = request.app.state.orchestrator

    # Publish transcript_chunk event to the multi-agent orchestrator
    results = await orchestrator.dispatch("transcript_chunk", {
        "transcript": body.transcript,
        "lesson_id": body.lesson_id or "unknown",
    })

    # For now, return mock analysis (real Gemini analysis in P03)
    analysis = {
        "grammar_score": 75,
        "vocabulary_score": 68,
        "filler_count": 2,
        "sentence_complexity_score": 65,
        "idiom_score": 40,
        "pace_wpm": 142,
        "coherence_score": 78,
        "confidence_score": 72,
        "mistakes": [
            {"timestamp": "0:15", "original": "more better", "correction": "better", "rule": "double comparative"},
        ],
        "missed_opportunities": [
            {"context": "led the team", "suggestion": "spearheaded the initiative", "type": "vocabulary"},
        ],
    }

    # Broadcast analysis via WebSocket if available
    ws_manager = getattr(request.app.state, "ws_manager", None)
    if ws_manager and body.lesson_id:
        await ws_manager.broadcast(body.lesson_id, {
            "type": "analysis_result",
            "data": analysis,
        })

    logger.info(f"analyze_speech called for lesson={body.lesson_id}, transcript_len={len(body.transcript)}")
    return analysis


@router.post("/tools/get_lesson_context")
async def get_lesson_context(body: GetLessonContextRequest):
    """Called by ElevenLabs agent to get current lesson objectives."""
    # Mock lesson context (real DB lookup in P04)
    return {
        "lesson_id": body.lesson_id or "diagnostic",
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

    # Publish lesson_end event
    await orchestrator.dispatch("lesson_end", {
        "final_transcript": body.final_transcript,
        "lesson_id": body.lesson_id or "unknown",
    })

    # Broadcast lesson end via WebSocket
    ws_manager = getattr(request.app.state, "ws_manager", None)
    if ws_manager and body.lesson_id:
        await ws_manager.broadcast(body.lesson_id, {
            "type": "lesson_end",
            "data": {"lesson_id": body.lesson_id},
        })

    logger.info(f"end_lesson called for lesson={body.lesson_id}, transcript_len={len(body.final_transcript)}")
    return {"status": "lesson_ended", "lesson_id": body.lesson_id}


# ---- Existing analysis endpoints ----

@router.get("/analysis/{lesson_id}")
async def get_analysis(lesson_id: str):
    # TODO: implement in P05
    return {"lesson_id": lesson_id, "analysis": {}}


@router.get("/analysis/{lesson_id}/report")
async def get_report(lesson_id: str):
    # TODO: implement in P05
    return {"lesson_id": lesson_id, "report": {}}
