"use client";

import { useState, useCallback } from "react";
import VoiceCall from "../../components/VoiceCall";

const AGENT_ID = process.env.NEXT_PUBLIC_ELEVENLABS_AGENT_ID ?? "";
const BACKEND_URL =
  process.env.NEXT_PUBLIC_BACKEND_URL ?? "http://localhost:8000";

export default function DiagnosticPage() {
  const [conversationId, setConversationId] = useState<string | null>(null);
  const [callState, setCallState] = useState<"idle" | "active" | "ended">(
    "idle",
  );
  const [error, setError] = useState<string | null>(null);

  const handleAudioCaptured = useCallback(async (blob: Blob) => {
    try {
      const form = new FormData();
      form.append("audio", blob, "diagnostic-recording.webm");
      form.append("user_id", "default-user");
      form.append("name", "Diagnostic Voice Sample");

      const res = await fetch(`${BACKEND_URL}/api/voice/clone`, {
        method: "POST",
        body: form,
      });

      if (!res.ok) {
        console.warn("Voice clone upload failed:", res.status);
      }
    } catch {
      console.warn("Could not upload audio for voice cloning");
    }
  }, []);

  return (
    <main className="flex flex-1 flex-col items-center justify-center gap-8 px-4">
      {/* Header */}
      <div className="text-center">
        <h1 className="text-3xl font-bold">Diagnostic Call</h1>
        <p className="mt-2 text-zinc-400">
          {callState === "idle"
            ? "Have a 2-minute conversation with Coach Alex so we can assess your level"
            : callState === "active"
              ? "Speak naturally — Coach Alex is listening and analyzing your speech"
              : "Great job! Your Speech DNA is being generated..."}
        </p>
      </div>

      {/* Voice call */}
      <div className="w-full max-w-md rounded-2xl border border-zinc-800 bg-surface p-8">
        <VoiceCall
          agentId={AGENT_ID}
          lessonId="diagnostic"
          onSessionStart={(id) => {
            setConversationId(id);
            setCallState("active");
          }}
          onSessionEnd={() => setCallState("ended")}
          onError={(msg) => setError(msg)}
          onAudioCaptured={handleAudioCaptured}
        />
      </div>

      {/* Error */}
      {error && (
        <div className="rounded-lg border border-red-800 bg-red-950/50 px-4 py-2 text-sm text-red-300">
          {error}
        </div>
      )}

      {/* Conversation ID for debugging */}
      {conversationId && (
        <p className="text-xs text-zinc-600">Session: {conversationId}</p>
      )}
    </main>
  );
}
