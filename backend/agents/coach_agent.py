import logging
from agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)


class CoachAgent(BaseAgent):
    """Manages conversation flow and coaching strategies based on live analysis."""

    def __init__(self):
        super().__init__("coach")
        # Track patterns across chunks per lesson
        self._pattern_tracker: dict[str, list[dict]] = {}

    async def handle_event(self, event_type: str, data: dict) -> dict | None:
        if event_type != "analysis_result":
            return None

        lesson_id = data.get("lesson_id", "unknown")
        analysis = data.get("analysis", {})

        grammar = analysis.get("grammar_score", 70)
        vocabulary = analysis.get("vocabulary_score", 70)
        mistakes = analysis.get("mistakes", [])

        # Track recurring mistakes
        self._pattern_tracker.setdefault(lesson_id, []).append({
            "grammar": grammar,
            "vocabulary": vocabulary,
            "mistakes": mistakes,
        })

        # Detect recurring error patterns
        recurring_errors = self._detect_recurring_errors(lesson_id)

        # Determine difficulty adjustment
        difficulty_adj = None
        reason = ""

        if grammar < 50:
            difficulty_adj = "easier"
            reason = "Grammar score below 50 — simplifying conversation difficulty."
        elif grammar > 85 and vocabulary > 80:
            difficulty_adj = "harder"
            reason = "Strong grammar and vocabulary — increasing challenge."
        elif len(recurring_errors) > 0:
            difficulty_adj = "focus"
            reason = f"Recurring errors detected: {', '.join(recurring_errors[:3])}. Focusing on these areas."

        result = {
            "lesson_id": lesson_id,
            "difficulty_adjustment": difficulty_adj,
            "reason": reason,
            "recurring_errors": recurring_errors,
            "chunk_count": len(self._pattern_tracker.get(lesson_id, [])),
        }

        if difficulty_adj:
            await self.emit("difficulty_adj", result)
            logger.info(f"[CoachAgent] Difficulty adjustment: {difficulty_adj} — {reason}")

        return result

    def _detect_recurring_errors(self, lesson_id: str) -> list[str]:
        """Find grammar rules that appear in multiple chunks."""
        history = self._pattern_tracker.get(lesson_id, [])
        if len(history) < 2:
            return []

        # Count how many chunks each rule appears in
        rule_counts: dict[str, int] = {}
        for entry in history:
            seen_rules = set()
            for mistake in entry.get("mistakes", []):
                rule = mistake.get("rule", "unknown")
                if rule not in seen_rules:
                    rule_counts[rule] = rule_counts.get(rule, 0) + 1
                    seen_rules.add(rule)

        # Return rules that appear in 2+ chunks
        return [rule for rule, count in rule_counts.items() if count >= 2]

    def clear_session(self, lesson_id: str):
        """Clear tracked patterns for a completed lesson."""
        self._pattern_tracker.pop(lesson_id, None)
