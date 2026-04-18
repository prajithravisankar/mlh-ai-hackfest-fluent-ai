export default function LessonPage({ params }: { params: Promise<{ id: string }> }) {
  return (
    <main className="flex flex-1 flex-col items-center justify-center">
      <h1 className="text-3xl font-bold">Live Lesson</h1>
      <p className="mt-2 text-zinc-400">Voice conversation in progress</p>
    </main>
  );
}
