const WS_URL =
  process.env.NEXT_PUBLIC_BACKEND_URL?.replace("http", "ws") ||
  "ws://localhost:8000";

export function connectWebSocket(
  lessonId: string,
  onMessage: (data: unknown) => void,
) {
  const ws = new WebSocket(`${WS_URL}/ws/lesson/${lessonId}`);

  ws.onopen = () => {
    console.log(`[WS] Connected to lesson ${lessonId}`);
  };

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    onMessage(data);
  };

  ws.onclose = () => {
    console.log(`[WS] Disconnected from lesson ${lessonId}`);
  };

  ws.onerror = (error) => {
    console.error("[WS] Error:", error);
  };

  return ws;
}
