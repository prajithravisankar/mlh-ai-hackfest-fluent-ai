export const ELEVENLABS_AGENT_ID =
  process.env.NEXT_PUBLIC_ELEVENLABS_AGENT_ID || "";

export function getElevenLabsConfig() {
  return {
    agentId: ELEVENLABS_AGENT_ID,
  };
}
