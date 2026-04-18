from agents.base_agent import BaseAgent


class AgentOrchestrator:
    """In-memory event bus that routes events to registered agents."""

    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}
        self._subscriptions: dict[str, list[str]] = {}

    def register(self, agent: BaseAgent, events: list[str]):
        agent.set_orchestrator(self)
        self._agents[agent.name] = agent
        for event in events:
            self._subscriptions.setdefault(event, []).append(agent.name)

    async def dispatch(self, event_type: str, data: dict, source: str = "system") -> list[dict]:
        results = []
        subscribers = self._subscriptions.get(event_type, [])
        for agent_name in subscribers:
            if agent_name == source:
                continue
            agent = self._agents[agent_name]
            result = await agent.handle_event(event_type, data)
            if result is not None:
                results.append({"agent": agent_name, "data": result})
        return results

    def get_agent(self, name: str) -> BaseAgent | None:
        return self._agents.get(name)
