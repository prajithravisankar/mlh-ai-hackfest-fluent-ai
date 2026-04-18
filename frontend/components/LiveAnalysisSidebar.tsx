"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import { connectWebSocket } from "../lib/websocket";
import type { AnalysisResult, Mistake, MissedOpportunity } from "../lib/types";

interface LiveAnalysisSidebarProps {
  lessonId: string;
  isActive: boolean;
}

function ScoreBar({
  label,
  value,
  displayValue,
}: {
  label: string;
  value: number;
  displayValue?: string;
}) {
  const color =
    value > 75
      ? "bg-emerald-500"
      : value > 50
        ? "bg-yellow-500"
        : "bg-red-500";
  const textColor =
    value > 75
      ? "text-emerald-400"
      : value > 50
        ? "text-yellow-400"
        : "text-red-400";

  return (
    <div className="space-y-1">
      <div className="flex justify-between text-sm">
        <span className="text-zinc-300">{label}</span>
        <span className={`font-mono font-semibold ${textColor}`}>
          {displayValue ?? `${Math.round(value)}%`}
        </span>
      </div>
      <div className="h-2 w-full overflow-hidden rounded-full bg-zinc-800">
        <div
          className={`h-full rounded-full transition-all duration-700 ease-out ${color}`}
          style={{ width: `${Math.min(100, Math.max(0, value))}%` }}
        />
      </div>
    </div>
  );
}

export default function LiveAnalysisSidebar({
  lessonId,
  isActive,
}: LiveAnalysisSidebarProps) {
  const [analysis, setAnalysis] = useState<AnalysisResult | null>(null);
  const [mistakes, setMistakes] = useState<Mistake[]>([]);
  const [missedOpportunities, setMissedOpportunities] = useState<
    MissedOpportunity[]
  >([]);
  const [chunkCount, setChunkCount] = useState(0);
  const wsRef = useRef<WebSocket | null>(null);
  const mistakesEndRef = useRef<HTMLDivElement>(null);

  const handleMessage = useCallback((data: unknown) => {
    const msg = data as { type: string; data: AnalysisResult };
    if (msg.type === "analysis_result" && msg.data) {
      setAnalysis(msg.data);
      setChunkCount((c) => c + 1);

      // Accumulate mistakes and missed opportunities
      if (msg.data.mistakes?.length) {
        setMistakes((prev) => [...prev, ...msg.data.mistakes].slice(-20));
      }
      if (msg.data.missed_opportunities?.length) {
        setMissedOpportunities((prev) =>
          [...prev, ...msg.data.missed_opportunities].slice(-10),
        );
      }
    }
  }, []);

  useEffect(() => {
    if (!isActive || !lessonId) return;

    const ws = connectWebSocket(lessonId, handleMessage);
    wsRef.current = ws;

    return () => {
      ws.close();
      wsRef.current = null;
    };
  }, [lessonId, isActive, handleMessage]);

  // Auto-scroll mistakes list
  useEffect(() => {
    mistakesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [mistakes]);

  if (!isActive) {
    return (
      <div className="flex h-full items-center justify-center rounded-2xl border border-zinc-800 bg-surface p-6">
        <p className="text-sm text-zinc-500">
          Start a call to see live analysis
        </p>
      </div>
    );
  }

  return (
    <div className="flex h-full flex-col gap-4 overflow-hidden rounded-2xl border border-zinc-800 bg-surface p-5">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h3 className="text-sm font-semibold text-zinc-200">Live Analysis</h3>
        {chunkCount > 0 && (
          <span className="rounded-full bg-accent/20 px-2 py-0.5 text-xs text-accent">
            {chunkCount} {chunkCount === 1 ? "update" : "updates"}
          </span>
        )}
      </div>

      {!analysis ? (
        <div className="flex flex-1 items-center justify-center">
          <div className="text-center">
            <div className="mx-auto mb-3 h-8 w-8 animate-pulse rounded-full bg-zinc-700" />
            <p className="text-sm text-zinc-500">Waiting for speech data...</p>
          </div>
        </div>
      ) : (
        <div className="flex flex-1 flex-col gap-4 overflow-y-auto">
          {/* Score bars */}
          <div className="space-y-3">
            <ScoreBar label="Grammar" value={analysis.grammar_score} />
            <ScoreBar label="Vocabulary" value={analysis.vocabulary_score} />
            <ScoreBar
              label="Filler Words"
              value={Math.max(0, 100 - analysis.filler_count * 10)}
              displayValue={`${analysis.filler_count} found`}
            />
            <ScoreBar label="Complexity" value={analysis.sentence_complexity_score} />
            <ScoreBar label="Idioms" value={analysis.idiom_score} />
            <ScoreBar
              label="Pace"
              value={
                analysis.pace_wpm >= 120 && analysis.pace_wpm <= 160
                  ? 100
                  : Math.max(0, 100 - Math.abs(analysis.pace_wpm - 140) * 1.5)
              }
              displayValue={`${analysis.pace_wpm} WPM`}
            />
            <ScoreBar label="Coherence" value={analysis.coherence_score} />
            <ScoreBar label="Confidence" value={analysis.confidence_score} />
          </div>

          {/* Mistakes */}
          {mistakes.length > 0 && (
            <div>
              <h4 className="mb-2 text-xs font-semibold uppercase tracking-wider text-red-400">
                Mistakes
              </h4>
              <div className="max-h-40 space-y-2 overflow-y-auto">
                {mistakes.map((m, i) => (
                  <div
                    key={`mistake-${i}`}
                    className="rounded-lg border border-red-900/50 bg-red-950/30 p-2 text-xs"
                  >
                    <div className="flex items-center gap-2">
                      <span className="text-zinc-500">{m.timestamp}</span>
                      <span className="text-red-300 line-through">
                        {m.original}
                      </span>
                      <span className="text-zinc-500">→</span>
                      <span className="text-emerald-300">{m.correction}</span>
                    </div>
                    <p className="mt-0.5 text-zinc-500">{m.rule}</p>
                  </div>
                ))}
                <div ref={mistakesEndRef} />
              </div>
            </div>
          )}

          {/* Missed Opportunities */}
          {missedOpportunities.length > 0 && (
            <div>
              <h4 className="mb-2 text-xs font-semibold uppercase tracking-wider text-blue-400">
                Missed Opportunities
              </h4>
              <div className="max-h-32 space-y-2 overflow-y-auto">
                {missedOpportunities.map((mo, i) => (
                  <div
                    key={`opp-${i}`}
                    className="rounded-lg border border-blue-900/50 bg-blue-950/30 p-2 text-xs"
                  >
                    <p className="text-zinc-400">
                      &ldquo;{mo.context}&rdquo;
                    </p>
                    <p className="mt-1 text-blue-300">
                      Try: &ldquo;{mo.suggestion}&rdquo;
                    </p>
                    <span className="mt-0.5 inline-block rounded bg-blue-900/50 px-1.5 py-0.5 text-[10px] text-blue-400">
                      {mo.type}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
