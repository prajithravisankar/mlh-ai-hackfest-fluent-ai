export default function ReplayPage({ params }: { params: Promise<{ id: string }> }) {
  return (
    <main className="flex flex-1 flex-col items-center justify-center">
      <h1 className="text-3xl font-bold">Call Replay</h1>
      <p className="mt-2 text-zinc-400">Annotated conversation replay</p>
    </main>
  );
}
