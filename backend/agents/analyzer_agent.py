from agents.base_agent import BaseAgent


class AnalyzerAgent(BaseAgent):
    """Runs real-time and post-lesson speech analysis using Gemini."""

    def __init__(self):
        super().__init__("analyzer")

    async def handle_event(self, event_type: str, data: dict) -> dict | None:
        # TODO: implement in P05
        return None
