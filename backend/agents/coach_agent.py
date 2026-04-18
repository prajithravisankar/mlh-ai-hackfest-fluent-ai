from agents.base_agent import BaseAgent


class CoachAgent(BaseAgent):
    """Manages conversation flow and coaching strategies."""

    def __init__(self):
        super().__init__("coach")

    async def handle_event(self, event_type: str, data: dict) -> dict | None:
        # TODO: implement in P04
        return None
