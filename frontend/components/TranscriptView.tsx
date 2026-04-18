"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import { connectWebSocket } from "../lib/websocket";
import type { Mistake, MissedOpportunity } from "../lib/types";

interface TranscriptEntry {
  id: string;
  speaker: "user" | "ai";
  text: string;
  timestamp: string;
  mistakes?: Mistake[];
  missedOpportunities?: MissedOpportunity[];
}

interface TranscriptViewProps {
  lessonId: string;
  isActive: boolean;
}

const FILLER_WORDS = [
  "um", "uh", "uhh", "umm", "like", "you know", "basically",
  "actually", "literally", "so", "well", "right", "I mean",
];

function highlightText(
  text: string,
  mistakes: Mistake[],
  missedOpportunities: MissedOpportunity[],
) {
  // Build a map of words/phrases to highlight
  const segments: { text: string; type: "normal" | "error" | "filler" | "suggestion"; tooltip?: string }[] = [];

  // Simple approach: split by words, check each
  let remaining = text;
  let cursor = 0;

  // Check for grammar errors (original phrases)
  const errorPhrases = mistakes.map((m) => ({
    phrase: m.original.toLowerCase(),
    correction: m.correction,
    rule: m.rule,
  }));

  // Build the highlighted output word by word
  const words = text.split(/(\s+)/);
  for (const word of words) {
    if (!word.trim()) {
      segments.push({ text: word, type: "normal" });
      continue;
    }

    const lower = word.toLowerCase().replace(/[.,!?;:]/g, "");

    // Check if it's a filler word
    if (FILLER_WORDS.includes(lower)) {
      segments.push({ text: word, type: "filler", tooltip: "Filler word" });
      continue;
    }

    // Check if part of an error
    const matchingError = errorPhrases.find((e) =>
      e.phrase.includes(lower) && lower.length > 2,
    );
    if (matchingError) {
      segments.push({
        text: word,
        type: "error",
        tooltip: `${matchingError.correction} (${matchingError.rule})`,
      });
      continue;
    }

    segments.push({ text: word, type: "normal" });
  }

  return segments;
}

export default function TranscriptView({ lessonId, isActive }: TranscriptViewProps) {
  const [entries, setEntries] = useState<TranscriptEntry[]>([]);
  const scrollRef = useRef<HTMLDivElement>(null);
  const wsRef = useRef<WebSocket | null>(null);
  const entryCountRef = useRef(0);

  const handleMessage = useCallback((data: unknown) => {
    const msg = data as { type: string; data: Record<string, unknown> };

    if (msg.type === "transcript_update") {
      const d = msg.data;
      entryCountRef.current += 1;
      const entry: TranscriptEntry = {
        id: `t-${entryCountRef.current}`,
        speaker: (d.speaker as string) === "user" ? "user" : "ai",
        text: d.text as string,
        timestamp: (d.timestamp as string) || new Date().toLocaleTimeString(),
      };
      setEntries((prev) => [...prev.slice(-50), entry]); // Keep last 50
    }

    if (msg.type === "analysis_result" && msg.data) {
      // Attach mistakes/missed opps to the most recent user entry
      const mistakes = (msg.data.mistakes as Mistake[]) || [];
      const missedOpps = (msg.data.missed_opportunities as MissedOpportunity[]) || [];

      if (mistakes.length || missedOpps.length) {
        setEntries((prev) => {
          const updated = [...prev];
          // Find last user entry
          for (let i = updated.length - 1; i >= 0; i--) {
            if (updated[i].speaker === "user") {
              updated[i] = {
                ...updated[i],
                mistakes,
                missedOpportunities: missedOpps,
              };
              break;
            }
          }
          return updated;
        });
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

  // Auto-scroll
  useEffect(() => {
    scrollRef.current?.scrollTo({
      top: scrollRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [entries]);

  if (!isActive) {
    return (
      <div className="flex h-full items-center justify-center rounded-2xl border border-zinc-800 bg-surface p-6">
        <p className="text-sm text-zinc-500">Transcript will appear here during the call</p>
      </div>
    );
  }

  return (
    <div className="flex h-full flex-col rounded-2xl border border-zinc-800 bg-surface">
      <div className="border-b border-zinc-800 px-4 py-3">
        <h3 className="text-sm font-semibold text-zinc-200">Live Transcript</h3>
      </div>

      <div ref={scrollRef} className="flex-1 space-y-3 overflow-y-auto p-4">
        {entries.length === 0 && (
          <p className="text-center text-sm text-zinc-600">
            Waiting for conversation...
          </p>
        )}

        {entries.map((entry) => {
          const segments = highlightText(
            entry.text,
            entry.mistakes || [],
            entry.missedOpportunities || [],
          );

          return (
            <div
              key={entry.id}
              className={`flex gap-3 ${entry.speaker === "user" ? "" : "flex-row-reverse"}`}
            >
              <div
                className={`max-w-[85%] rounded-xl px-3 py-2 text-sm ${
                  entry.speaker === "user"
                    ? "bg-zinc-800 text-zinc-200"
                    : "bg-accent/20 text-zinc-200"
                }`}
              >
                <div className="mb-1 flex items-center gap-2">
                  <span className="text-[10px] font-semibold uppercase tracking-wider text-zinc-500">
                    {entry.speaker === "user" ? "You" : "AI"}
                  </span>
                  <span className="text-[10px] text-zinc-600">{entry.timestamp}</span>
                </div>
                <p className="leading-relaxed">
                  {segments.map((seg, i) => {
                    if (seg.type === "error") {
                      return (
                        <span
                          key={i}
                          className="relative cursor-help border-b-2 border-red-500 text-red-300"
                          title={seg.tooltip}
                        >
                          {seg.text}
                        </span>
                      );
                    }
                    if (seg.type === "filler") {
                      return (
                        <span
                          key={i}
                          className="rounded bg-yellow-900/40 px-0.5 text-yellow-300"
                          title={seg.tooltip}
                        >
                          {seg.text}
                        </span>
                      );
                    }
                    return <span key={i}>{seg.text}</span>;
                  })}
                </p>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
