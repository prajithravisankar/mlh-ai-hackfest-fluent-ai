"use client";

import { use, useState, useEffect, useCallback, useRef } from "react";
import { useRouter } from "next/navigation";
import VoiceCall from "../../../components/VoiceCall";
import LiveAnalysisSidebar from "../../../components/LiveAnalysisSidebar";
import TranscriptView from "../../../components/TranscriptView";
import { startLesson, endLesson } from "../../../lib/api";

const AGENT_ID = process.env.NEXT_PUBLIC_ELEVENLABS_AGENT_ID || "";

interface LessonConfig {
  lesson_id: string;
  title: string;
  character: {
    name: string;
    role: string;
    style: string;
    avatar: string;
  };
  objectives: string[];
  pressure_mode: boolean;
}

export default function LessonPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = use(params);
  const router = useRouter();

  const [isCallActive, setIsCallActive] = useState(false);
  const [lessonConfig, setLessonConfig] = useState<LessonConfig | null>(null);
  const [pressureMode, setPressureMode] = useState(false);
  const [elapsed, setElapsed] = useState(0);
  const [isEnding, setIsEnding] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // Timer
  useEffect(() => {
    if (isCallActive) {
      timerRef.current = setInterval(() => setElapsed((s) => s + 1), 1000);
    } else {
      if (timerRef.current) clearInterval(timerRef.current);
    }
    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [isCallActive]);

  const formatTime = (s: number) => {
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return `${m}:${sec.toString().padStart(2, "0")}`;
  };

  // Initialize lesson on mount
  useEffect(() => {
    const init = async () => {
      try {
        // Read config from URL search params or use defaults
        const urlParams = new URLSearchParams(window.location.search);
        const character = urlParams.get("character") || "coach_alex";
        const title = urlParams.get("title") || "Conversation Practice";

        const config = await startLesson("user_1", {
          title,
          character,
          objectives: ["Improve overall fluency", "Practice natural conversation"],
          pressure_mode: pressureMode,
        });
        setLessonConfig(config);
      } catch (err) {
        console.error("Failed to start lesson:", err);
        // Set a fallback config so the page still renders
        setLessonConfig({
          lesson_id: id,
          title: "Conversation Practice",
          character: { name: "Coach Alex", role: "English Coach", style: "warm", avatar: "🎤" },
          objectives: ["Improve overall fluency"],
          pressure_mode: false,
        });
      }
    };
    init();
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const lessonId = lessonConfig?.lesson_id || id;

  const handleEndLesson = useCallback(async () => {
    setIsEnding(true);
    try {
      await endLesson(lessonId);
    } catch (err) {
      console.error("Failed to end lesson:", err);
    }
    router.push(`/report/${lessonId}`);
  }, [lessonId, router]);

  return (
    <main className="flex flex-1 flex-col overflow-hidden">
      {/* Top Bar */}
      <div className="flex items-center justify-between border-b border-zinc-800 bg-surface px-6 py-3">
        <div className="flex items-center gap-4">
          {/* Character Info */}
          {lessonConfig && (
            <div className="flex items-center gap-3">
              <span className="text-2xl">{lessonConfig.character.avatar}</span>
              <div>
                <h1 className="text-sm font-semibold text-zinc-100">
                  {lessonConfig.title}
                </h1>
                <p className="text-xs text-zinc-400">
                  with {lessonConfig.character.name} · {lessonConfig.character.role}
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Center: Timer */}
        <div className="flex items-center gap-4">
          <div
            className={`rounded-lg px-4 py-1.5 font-mono text-lg font-bold ${
              isCallActive ? "bg-accent/20 text-accent" : "bg-zinc-800 text-zinc-500"
            }`}
          >
            {formatTime(elapsed)}
          </div>
        </div>

        {/* Right: Controls */}
        <div className="flex items-center gap-3">
          {/* Pressure Mode Toggle */}
          <button
            onClick={() => setPressureMode(!pressureMode)}
            disabled={isCallActive}
            className={`flex items-center gap-2 rounded-lg px-3 py-1.5 text-xs font-medium transition-all ${
              pressureMode
                ? "bg-danger/20 text-danger border border-danger/40"
                : "bg-zinc-800 text-zinc-400 border border-zinc-700 hover:border-zinc-600"
            } ${isCallActive ? "opacity-50 cursor-not-allowed" : ""}`}
          >
            <span>🔥</span>
            <span>Pressure</span>
            <div
              className={`h-3 w-6 rounded-full transition-colors ${
                pressureMode ? "bg-danger" : "bg-zinc-600"
              }`}
            >
              <div
                className={`h-3 w-3 rounded-full bg-white transition-transform ${
                  pressureMode ? "translate-x-3" : "translate-x-0"
                }`}
              />
            </div>
          </button>

          {/* End Lesson Button */}
          {isCallActive && (
            <button
              onClick={handleEndLesson}
              disabled={isEnding}
              className="rounded-lg bg-danger px-4 py-1.5 text-sm font-semibold text-white transition-all hover:bg-red-400 disabled:opacity-50"
            >
              {isEnding ? "Ending..." : "End Lesson"}
            </button>
          )}
        </div>
      </div>

      {/* Objectives Banner */}
      {lessonConfig && !isCallActive && (
        <div className="border-b border-zinc-800 bg-zinc-900/50 px-6 py-2">
          <div className="flex flex-wrap gap-2">
            <span className="text-xs font-semibold text-zinc-500">Objectives:</span>
            {lessonConfig.objectives.map((obj, i) => (
              <span
                key={i}
                className="rounded-full bg-accent/10 px-2.5 py-0.5 text-xs text-accent"
              >
                {obj}
              </span>
            ))}
          </div>
        </div>
      )}

      {/* Main Content */}
      <div className="flex flex-1 gap-4 overflow-hidden p-4">
        {/* Left Column: Voice Call + Transcript */}
        <div className="flex flex-1 flex-col gap-4">
          {/* Voice Call */}
          <div className="flex items-center justify-center rounded-2xl border border-zinc-800 bg-surface p-6">
            <VoiceCall
              agentId={AGENT_ID}
              lessonId={lessonId}
              onSessionStart={() => {
                setIsCallActive(true);
                setElapsed(0);
              }}
              onSessionEnd={() => setIsCallActive(false)}
            />
          </div>

          {/* Transcript */}
          <div className="flex-1 min-h-0">
            <TranscriptView lessonId={lessonId} isActive={isCallActive} />
          </div>
        </div>

        {/* Right Column: Live Analysis Sidebar */}
        <div className="w-80 shrink-0">
          <LiveAnalysisSidebar lessonId={lessonId} isActive={isCallActive} />
        </div>
      </div>
    </main>
  );
}
