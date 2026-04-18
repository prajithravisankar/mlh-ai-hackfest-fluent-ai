"use client";

import { use, useState } from "react";
import VoiceCall from "../../../components/VoiceCall";
import LiveAnalysisSidebar from "../../../components/LiveAnalysisSidebar";

const AGENT_ID = process.env.NEXT_PUBLIC_ELEVENLABS_AGENT_ID || "";

export default function LessonPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = use(params);
  const [isCallActive, setIsCallActive] = useState(false);

  return (
    <main className="flex flex-1 gap-6 p-6">
      {/* Left: Voice call area */}
      <div className="flex flex-1 flex-col">
        <VoiceCall
          agentId={AGENT_ID}
          lessonId={id}
          onSessionStart={() => setIsCallActive(true)}
          onSessionEnd={() => setIsCallActive(false)}
        />
      </div>

      {/* Right: Live analysis sidebar */}
      <div className="w-80 shrink-0">
        <LiveAnalysisSidebar lessonId={id} isActive={isCallActive} />
      </div>
    </main>
  );
}
