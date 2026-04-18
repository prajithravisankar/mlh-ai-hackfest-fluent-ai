const BACKEND_URL =
  process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

export async function fetchHealth() {
  const res = await fetch(`${BACKEND_URL}/api/health`);
  return res.json();
}

export async function startLesson(
  userId: string,
  config: Record<string, unknown>,
) {
  const res = await fetch(`${BACKEND_URL}/api/lessons/start`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, ...config }),
  });
  return res.json();
}

export async function endLesson(lessonId: string) {
  const res = await fetch(`${BACKEND_URL}/api/lessons/${lessonId}/end`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  });
  return res.json();
}

export async function getLesson(lessonId: string) {
  const res = await fetch(`${BACKEND_URL}/api/lessons/${lessonId}`);
  return res.json();
}

export async function getReport(lessonId: string) {
  // TODO: implement in P05
  return {};
}

export async function getDNA(userId: string) {
  // TODO: implement in P06
  return {};
}

export async function getRoadmap(userId: string) {
  // TODO: implement in P08
  return {};
}

export async function getProfile(userId: string) {
  // TODO: implement in P07
  return {};
}
