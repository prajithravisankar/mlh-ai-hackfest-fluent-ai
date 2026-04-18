from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Abstract base for all FluentAI agents."""

    def __init__(self, name: str):
        self.name = name
        self._orchestrator = None

    def set_orchestrator(self, orchestrator):
        self._orchestrator = orchestrator

    async def emit(self, event_type: str, data: dict):
        if self._orchestrator:
            await self._orchestrator.dispatch(event_type, data, source=self.name)

    @abstractmethod
    async def handle_event(self, event_type: str, data: dict) -> dict | None:
        """Handle an incoming event. Return optional response data."""
        ...
