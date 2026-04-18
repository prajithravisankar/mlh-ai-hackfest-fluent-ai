import logging
from agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)


class DNAAgent(BaseAgent):
    """Computes and updates Speech DNA profiles in real-time from analysis results."""

    def __init__(self):
        super().__init__("dna")
        # Running averages per lesson — maps lesson_id → list of score dicts
        self._running: dict[str, list[dict]] = {}

    async def handle_event(self, event_type: str, data: dict) -> dict | None:
        if event_type != "analysis_result":
            return None

        lesson_id = data.get("lesson_id", "unknown")
        analysis = data.get("analysis", {})

        # Extract score dimensions from analysis
        scores = {
            "grammar": analysis.get("grammar_score", 0),
            "vocabulary": analysis.get("vocabulary_score", 0),
            "filler_words": max(0, 100 - analysis.get("filler_count", 0) * 10),  # Convert count → 0-100 (fewer fillers = higher)
            "sentence_complexity": analysis.get("sentence_complexity_score", 0),
            "idiom_usage": analysis.get("idiom_score", 0),
            "speaking_pace": self._pace_to_score(analysis.get("pace_wpm", 130)),
            "coherence": analysis.get("coherence_score", 0),
            "confidence": analysis.get("confidence_score", 0),
        }

        # Append to running list for this lesson
        self._running.setdefault(lesson_id, []).append(scores)

        # Compute running averages
        dna_snapshot = self._compute_averages(lesson_id)

        # Publish dna_update event
        await self.emit("dna_update", {
            "lesson_id": lesson_id,
            "dna": dna_snapshot,
            "chunk_count": len(self._running[lesson_id]),
        })

        logger.info(
            f"[DNAAgent] DNA updated for lesson={lesson_id}: "
            f"grammar={dna_snapshot['grammar']}, vocab={dna_snapshot['vocabulary']}"
        )

        return dna_snapshot

    def _compute_averages(self, lesson_id: str) -> dict:
        """Compute running average DNA from all chunks in this lesson."""
        entries = self._running.get(lesson_id, [])
        if not entries:
            return {dim: 0 for dim in [
                "grammar", "vocabulary", "filler_words", "sentence_complexity",
                "idiom_usage", "speaking_pace", "coherence", "confidence",
            ]}

        n = len(entries)
        dimensions = entries[0].keys()
        return {
            dim: round(sum(e[dim] for e in entries) / n, 1)
            for dim in dimensions
        }

    @staticmethod
    def _pace_to_score(wpm: int) -> float:
        """Convert WPM to a 0-100 score. Optimal range: 120-160 WPM."""
        if 120 <= wpm <= 160:
            return 100.0
        elif wpm < 120:
            # Penalize slow pace
            return max(0, 100 - (120 - wpm) * 1.5)
        else:
            # Penalize fast pace
            return max(0, 100 - (wpm - 160) * 1.5)

    def get_current_dna(self, lesson_id: str) -> dict:
        """Get the current running DNA for a lesson."""
        return self._compute_averages(lesson_id)

    def clear_session(self, lesson_id: str):
        """Clear running data for a completed lesson."""
        self._running.pop(lesson_id, None)
