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
  // TODO: implement in P04
  return { lesson_id: "" };
}

export async function endLesson(lessonId: string) {
  // TODO: implement in P04
  return { lesson_id: lessonId };
}

export async function getLesson(lessonId: string) {
  // TODO: implement in P04
  return {};
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
