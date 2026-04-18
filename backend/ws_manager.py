import json
import logging
from typing import Dict, Set

from fastapi import WebSocket

logger = logging.getLogger(__name__)


class WebSocketManager:
    """Manages WebSocket connections grouped by lesson_id."""

    def __init__(self):
        self._connections: Dict[str, Set[WebSocket]] = {}

    async def connect(self, lesson_id: str, ws: WebSocket):
        await ws.accept()
        self._connections.setdefault(lesson_id, set()).add(ws)
        logger.info(f"[WS] Client connected to lesson {lesson_id} (total: {len(self._connections[lesson_id])})")

    def disconnect(self, lesson_id: str, ws: WebSocket):
        if lesson_id in self._connections:
            self._connections[lesson_id].discard(ws)
            if not self._connections[lesson_id]:
                del self._connections[lesson_id]
        logger.info(f"[WS] Client disconnected from lesson {lesson_id}")

    async def broadcast(self, lesson_id: str, data: dict):
        """Send a JSON message to all clients connected to a lesson."""
        if lesson_id not in self._connections:
            return
        payload = json.dumps(data)
        dead = []
        for ws in self._connections[lesson_id]:
            try:
                await ws.send_text(payload)
            except Exception:
                dead.append(ws)
        for ws in dead:
            self._connections[lesson_id].discard(ws)

    async def send_personal(self, ws: WebSocket, data: dict):
        """Send a message to a specific client."""
        await ws.send_text(json.dumps(data))

    @property
    def active_connections(self) -> int:
        return sum(len(v) for v in self._connections.values())
