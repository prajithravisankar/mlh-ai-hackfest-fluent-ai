import json
import logging
import os
from typing import Optional

from google import genai

logger = logging.getLogger(__name__)

ANALYSIS_PROMPT = """You are an expert English language analysis engine for FluentAI, an AI English speaking coach.

Analyze the following transcript chunk from a spoken English conversation. Evaluate across these 8 dimensions, scoring each from 0 to 100:

1. **grammar_score** — Grammar accuracy. Detect errors like wrong tense, subject-verb disagreement, article misuse, double comparatives, etc.
2. **vocabulary_score** — Vocabulary depth and diversity. Penalize overuse of simple words (good, bad, nice, thing). Reward advanced/precise vocabulary.
3. **filler_count** — Count filler words: "um", "uh", "like" (non-comparative), "basically", "you know", "so" (as filler), "right", "I mean", "kind of", "sort of", "actually" (as filler). Return the integer count.
4. **sentence_complexity_score** — Sentence structure variety. Reward subordinate clauses, varied structures. Penalize all-simple sentences.
5. **idiom_score** — Natural use of English idioms and collocations. Score 0 if none used, higher if used appropriately.
6. **pace_wpm** — Estimate words per minute from the transcript length and assumed speaking duration. If you cannot estimate, use 130.
7. **coherence_score** — Logical flow, transitions, structured responses (e.g., STAR method). Penalize rambling or tangents.
8. **confidence_score** — Detect hedging ("I think maybe", "I'm not sure but"), uptalk patterns, trailing off. Higher = more confident.

Also identify:
- **mistakes**: Array of specific grammar/usage errors. Each has: timestamp (estimate position like "0:15"), original (what they said), correction (what they should say), rule (grammar rule name).
- **missed_opportunities**: Array of places where better vocabulary, idioms, or phrasing could be used. Each has: context (what they said), suggestion (better version), type ("vocabulary" | "idiom" | "structure").

{dna_context}

{lesson_context}

**TRANSCRIPT TO ANALYZE:**
\"\"\"{transcript}\"\"\"

**RESPOND WITH ONLY valid JSON** matching this exact schema (no markdown, no explanation):
{{
  "grammar_score": <0-100>,
  "vocabulary_score": <0-100>,
  "filler_count": <integer>,
  "sentence_complexity_score": <0-100>,
  "idiom_score": <0-100>,
  "pace_wpm": <integer>,
  "coherence_score": <0-100>,
  "confidence_score": <0-100>,
  "mistakes": [
    {{"timestamp": "<time>", "original": "<text>", "correction": "<text>", "rule": "<rule>"}}
  ],
  "missed_opportunities": [
    {{"context": "<text>", "suggestion": "<text>", "type": "<vocabulary|idiom|structure>"}}
  ]
}}"""

FALLBACK_ANALYSIS = {
    "grammar_score": 60,
    "vocabulary_score": 55,
    "filler_count": 3,
    "sentence_complexity_score": 50,
    "idiom_score": 30,
    "pace_wpm": 130,
    "coherence_score": 60,
    "confidence_score": 55,
    "mistakes": [],
    "missed_opportunities": [],
}

REQUIRED_FIELDS = [
    "grammar_score", "vocabulary_score", "filler_count",
    "sentence_complexity_score", "idiom_score", "pace_wpm",
    "coherence_score", "confidence_score", "mistakes", "missed_opportunities",
]


class GeminiAnalyzer:
    """Analyzes speech transcripts using Gemini 2.5 Flash."""

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY", "")
        self._client = genai.Client(api_key=api_key)
        self._model = "gemini-2.5-flash-preview-05-20"

    async def analyze_transcript_chunk(
        self,
        transcript: str,
        speech_dna: Optional[dict] = None,
        lesson_objective: Optional[str] = None,
    ) -> dict:
        """Analyze a transcript chunk and return structured analysis JSON."""
        if not transcript or not transcript.strip():
            return dict(FALLBACK_ANALYSIS)

        # Build context sections
        dna_context = ""
        if speech_dna:
            dna_context = (
                f"**USER'S CURRENT SPEECH DNA (for context — flag recurring weaknesses):**\n"
                f"Grammar: {speech_dna.get('grammar', 'N/A')}, "
                f"Vocabulary: {speech_dna.get('vocabulary', 'N/A')}, "
                f"Filler Words: {speech_dna.get('filler_words', 'N/A')}, "
                f"Complexity: {speech_dna.get('sentence_complexity', 'N/A')}, "
                f"Idioms: {speech_dna.get('idiom_usage', 'N/A')}, "
                f"Pace: {speech_dna.get('speaking_pace', 'N/A')}, "
                f"Coherence: {speech_dna.get('coherence', 'N/A')}, "
                f"Confidence: {speech_dna.get('confidence', 'N/A')}"
            )

        lesson_context = ""
        if lesson_objective:
            lesson_context = f"**LESSON OBJECTIVE:** {lesson_objective}"

        prompt = ANALYSIS_PROMPT.format(
            transcript=transcript,
            dna_context=dna_context,
            lesson_context=lesson_context,
        )

        try:
            response = self._client.models.generate_content(
                model=self._model,
                contents=prompt,
            )
            raw_text = response.text.strip()

            # Strip markdown code fences if present
            if raw_text.startswith("```"):
                lines = raw_text.split("\n")
                # Remove first line (```json) and last line (```)
                lines = [l for l in lines if not l.strip().startswith("```")]
                raw_text = "\n".join(lines)

            analysis = json.loads(raw_text)
            return self._validate_analysis(analysis)

        except json.JSONDecodeError as e:
            logger.warning(f"Gemini returned invalid JSON: {e}")
            return dict(FALLBACK_ANALYSIS)
        except Exception as e:
            logger.error(f"Gemini analysis failed: {e}")
            return dict(FALLBACK_ANALYSIS)

    def _validate_analysis(self, analysis: dict) -> dict:
        """Validate and sanitize analysis JSON. Fill missing fields with defaults."""
        result = dict(FALLBACK_ANALYSIS)
        for field in REQUIRED_FIELDS:
            if field in analysis:
                result[field] = analysis[field]

        # Clamp scores to 0-100
        score_fields = [
            "grammar_score", "vocabulary_score", "sentence_complexity_score",
            "idiom_score", "coherence_score", "confidence_score",
        ]
        for f in score_fields:
            val = result[f]
            if isinstance(val, (int, float)):
                result[f] = max(0, min(100, round(val)))
            else:
                result[f] = FALLBACK_ANALYSIS[f]

        # Ensure filler_count is non-negative int
        if isinstance(result["filler_count"], (int, float)):
            result["filler_count"] = max(0, int(result["filler_count"]))
        else:
            result["filler_count"] = FALLBACK_ANALYSIS["filler_count"]

        # Ensure pace_wpm is positive int
        if isinstance(result["pace_wpm"], (int, float)):
            result["pace_wpm"] = max(50, min(300, int(result["pace_wpm"])))
        else:
            result["pace_wpm"] = FALLBACK_ANALYSIS["pace_wpm"]

        # Ensure arrays
        if not isinstance(result["mistakes"], list):
            result["mistakes"] = []
        if not isinstance(result["missed_opportunities"], list):
            result["missed_opportunities"] = []

        return result
