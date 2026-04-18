import logging
from agents.base_agent import BaseAgent
from services.gemini_analyzer import GeminiAnalyzer

logger = logging.getLogger(__name__)


class AnalyzerAgent(BaseAgent):
    """Runs real-time speech analysis using Gemini on transcript chunks."""

    def __init__(self):
        super().__init__("analyzer")
        self._analyzer = GeminiAnalyzer()
        # Running buffer of analysis results per lesson
        self._session_buffer: dict[str, list[dict]] = {}

    async def handle_event(self, event_type: str, data: dict) -> dict | None:
        if event_type != "transcript_chunk":
            return None

        transcript = data.get("transcript", "")
        lesson_id = data.get("lesson_id", "unknown")
        speech_dna = data.get("speech_dna")
        lesson_objective = data.get("lesson_objective")

        logger.info(f"[AnalyzerAgent] Analyzing chunk for lesson={lesson_id}, len={len(transcript)}")

        # Run Gemini analysis
        analysis = await self._analyzer.analyze_transcript_chunk(
            transcript=transcript,
            speech_dna=speech_dna,
            lesson_objective=lesson_objective,
        )

        # Store in session buffer
        self._session_buffer.setdefault(lesson_id, []).append(analysis)

        # Publish analysis_result event for other agents (Coach, DNA, etc.)
        await self.emit("analysis_result", {
            "lesson_id": lesson_id,
            "analysis": analysis,
            "chunk_index": len(self._session_buffer[lesson_id]) - 1,
        })

        logger.info(
            f"[AnalyzerAgent] Published analysis_result: grammar={analysis['grammar_score']}, "
            f"vocab={analysis['vocabulary_score']}, fillers={analysis['filler_count']}"
        )

        return analysis

    def get_session_buffer(self, lesson_id: str) -> list[dict]:
        """Get all analysis chunks for a lesson session."""
        return self._session_buffer.get(lesson_id, [])

    def clear_session(self, lesson_id: str):
        """Clear the buffer for a completed lesson."""
        self._session_buffer.pop(lesson_id, None)
