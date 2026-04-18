"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import {
  ConversationProvider,
  useConversationControls,
  useConversationStatus,
} from "@elevenlabs/react";
import WaveformVisualizer from "./WaveformVisualizer";

interface VoiceCallProps {
  agentId: string;
  lessonId?: string;
  onSessionStart?: (conversationId: string) => void;
  onSessionEnd?: () => void;
  onError?: (message: string) => void;
  /** Callback with raw audio blob after call ends (for voice cloning) */
  onAudioCaptured?: (blob: Blob) => void;
}

function VoiceCallInner({
  lessonId,
  onSessionStart,
  onSessionEnd,
  onError,
  onAudioCaptured,
}: Omit<VoiceCallProps, "agentId">) {
  const { startSession, endSession } = useConversationControls();
  const { status } = useConversationStatus();
  const [elapsed, setElapsed] = useState(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);

  // Timer
  useEffect(() => {
    if (status === "connected") {
      timerRef.current = setInterval(() => setElapsed((s) => s + 1), 1000);
    } else {
      if (timerRef.current) clearInterval(timerRef.current);
    }
    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [status]);

  const formatTime = (s: number) => {
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return `${m}:${sec.toString().padStart(2, "0")}`;
  };

  // Start audio capture for voice cloning
  const startAudioCapture = useCallback(async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream, { mimeType: "audio/webm" });
      audioChunksRef.current = [];

      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) audioChunksRef.current.push(e.data);
      };

      recorder.onstop = () => {
        const blob = new Blob(audioChunksRef.current, { type: "audio/webm" });
        if (onAudioCaptured && blob.size > 0) {
          onAudioCaptured(blob);
        }
        stream.getTracks().forEach((t) => t.stop());
      };

      recorder.start(1000); // Collect in 1s chunks
      mediaRecorderRef.current = recorder;
    } catch {
      console.warn("Could not capture audio for cloning");
    }
  }, [onAudioCaptured]);

  const handleStart = async () => {
    // Start audio capture in parallel with session
    startAudioCapture();

    startSession({
      onConnect: ({ conversationId }) => {
        onSessionStart?.(conversationId);
      },
      onError: (message) => {
        onError?.(message);
      },
    });
  };

  const handleEnd = () => {
    endSession();

    // Stop audio recorder
    if (
      mediaRecorderRef.current &&
      mediaRecorderRef.current.state !== "inactive"
    ) {
      mediaRecorderRef.current.stop();
    }

    onSessionEnd?.();
  };

  const statusLabels: Record<string, string> = {
    disconnected: "Ready",
    connecting: "Connecting...",
    connected: "In Call",
    error: "Error",
  };

  const statusColors: Record<string, string> = {
    disconnected: "text-zinc-400",
    connecting: "text-warning",
    connected: "text-success",
    error: "text-danger",
  };

  return (
    <div className="flex flex-col items-center gap-6">
      {/* Status indicator */}
      <div className="flex items-center gap-3">
        <div
          className={`h-3 w-3 rounded-full ${status === "connected" ? "bg-success animate-pulse" : status === "connecting" ? "bg-warning animate-pulse" : status === "error" ? "bg-danger" : "bg-zinc-600"}`}
        />
        <span className={`text-sm font-medium ${statusColors[status] || "text-zinc-400"}`}>
          {statusLabels[status] || status}
        </span>
        {status === "connected" && (
          <span className="text-sm text-zinc-500 font-mono">
            {formatTime(elapsed)}
          </span>
        )}
      </div>

      {/* Waveform visualization */}
      {status === "connected" && <WaveformVisualizer isActive={true} />}

      {/* Controls */}
      <div className="flex items-center gap-4">
        {status === "disconnected" || status === "error" ? (
          <button
            onClick={handleStart}
            className="rounded-full bg-accent px-8 py-3 text-lg font-semibold text-white transition-all hover:bg-accent-light hover:scale-105 active:scale-95"
          >
            Start Call
          </button>
        ) : status === "connected" ? (
          <button
            onClick={handleEnd}
            className="rounded-full bg-danger px-8 py-3 text-lg font-semibold text-white transition-all hover:bg-red-400 hover:scale-105 active:scale-95"
          >
            End Call
          </button>
        ) : (
          <button
            disabled
            className="rounded-full bg-zinc-700 px-8 py-3 text-lg font-semibold text-zinc-400 cursor-not-allowed"
          >
            Connecting...
          </button>
        )}
      </div>

      {/* Lesson context */}
      {lessonId && (
        <p className="text-xs text-zinc-600">Lesson: {lessonId}</p>
      )}
    </div>
  );
}

export default function VoiceCall(props: VoiceCallProps) {
  return (
    <ConversationProvider agentId={props.agentId}>
      <VoiceCallInner {...props} />
    </ConversationProvider>
  );
}
