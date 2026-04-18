from agents.base_agent import BaseAgent


class ReportAgent(BaseAgent):
    """Generates post-lesson report cards."""

    def __init__(self):
        super().__init__("report")

    async def handle_event(self, event_type: str, data: dict) -> dict | None:
        # TODO: implement in P05
        return None
