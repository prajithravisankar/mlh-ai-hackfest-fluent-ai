import Link from "next/link";

export default function Home() {
  return (
    <main className="flex flex-1 flex-col items-center justify-center px-4">
      <div className="flex flex-col items-center gap-8 text-center">
        <h1 className="text-5xl font-bold tracking-tight">
          Stop typing English.<br />
          <span className="text-accent-light">Start speaking it.</span>
        </h1>
        <p className="max-w-md text-lg text-zinc-400">
          AI-powered speaking coach that listens, analyzes, and helps you sound like a native speaker.
        </p>
        <Link
          href="/diagnostic"
          className="rounded-full bg-accent px-8 py-3 text-lg font-semibold text-white transition-colors hover:bg-accent-light"
        >
          Start Free Diagnostic
        </Link>
      </div>
    </main>
  );
}
