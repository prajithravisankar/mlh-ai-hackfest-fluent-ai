# Evaluation Rubrics — Speech DNA Dimensions

> Scoring criteria used by Gemini to evaluate user speech across 8 dimensions. Each dimension is scored 0–100.

---

## 1. Grammar Accuracy (0–100)

Measures correctness of sentence structure, verb forms, tense usage, agreement, and syntax.

| Score Range | Label            | Criteria                                                                                                                       |
| ----------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 90–100      | **Expert**       | Near-native accuracy. Occasional minor slips only. Complex structures used correctly (conditionals, passive, reported speech). |
| 75–89       | **Advanced**     | Mostly correct. Minor errors in complex structures but self-corrects. Doesn't impede understanding.                            |
| 50–74       | **Intermediate** | Noticeable errors in tense, agreement, or articles. Core meaning is clear but grammar is inconsistent.                         |
| 25–49       | **Developing**   | Frequent errors that sometimes confuse meaning. Limited to simple sentence structures.                                         |
| 0–24        | **Beginner**     | Pervasive errors. Sentences are often fragmented or unintelligible.                                                            |

**What to flag:** Subject-verb disagreement, wrong tense, missing articles, double negatives, incorrect conditionals, dangling modifiers.

---

## 2. Vocabulary Range (0–100)

Measures diversity of word choices, use of precise/advanced vocabulary, and avoidance of repetition.

| Score Range | Label            | Criteria                                                                                      |
| ----------- | ---------------- | --------------------------------------------------------------------------------------------- |
| 90–100      | **Expert**       | Rich, varied vocabulary. Uses precise words, academic terms, and nuanced synonyms naturally.  |
| 75–89       | **Advanced**     | Good range. Occasionally uses advanced vocabulary. Avoids most word repetition.               |
| 50–74       | **Intermediate** | Adequate vocabulary for common topics. Relies on basic/common words. Some repetition.         |
| 25–49       | **Developing**   | Limited vocabulary. Frequently repeats words. Struggles with topic-specific terms.            |
| 0–24        | **Beginner**     | Very restricted vocabulary. Uses only the most basic words. Frequent "I don't know the word." |

**What to flag:** Overused simple words (good, bad, nice, thing, stuff), missed opportunities for precise vocabulary, repeated words within 3 sentences.

**Bonus signals:** Collocations used correctly (make a decision vs. do a decision), topic-appropriate jargon, varied synonyms.

---

## 3. Filler Word Usage (0–100)

Measures how clean the speech is — absence of um, uh, like, you know, basically, actually, right, so (when used as fillers).

| Score Range | Label             | Criteria                                                                                  |
| ----------- | ----------------- | ----------------------------------------------------------------------------------------- |
| 90–100      | **Clean Speaker** | 0–2 fillers per minute. Speech flows naturally with purposeful pauses instead of fillers. |
| 75–89       | **Mostly Clean**  | 3–5 fillers per minute. Occasional fillers but they don't distract.                       |
| 50–74       | **Moderate**      | 6–10 fillers per minute. Noticeable pattern that slightly distracts from content.         |
| 25–49       | **Frequent**      | 11–15 fillers per minute. Fillers become distracting and reduce perceived confidence.     |
| 0–24        | **Heavy**         | 16+ fillers per minute. Speech is dominated by fillers, difficult to follow content.      |

**What to flag:** Each individual filler with timestamp. Patterns (e.g., "um" at the start of every sentence, "like" mid-sentence, "you know" as a crutch).

**Note:** Distinguish between filler "like" and meaningful "like" (comparison). Same for "so" (filler vs. conjunction).

---

## 4. Sentence Complexity (0–100)

Measures structural sophistication — use of compound/complex sentences, subordinate clauses, varied openers.

| Score Range | Label            | Criteria                                                                                                                    |
| ----------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 90–100      | **Expert**       | Naturally varies between simple, compound, and complex sentences. Uses relative clauses, conditionals, participial phrases. |
| 75–89       | **Advanced**     | Uses compound and some complex sentences. Occasionally starts with subordinate clauses or transitions.                      |
| 50–74       | **Intermediate** | Mostly simple and compound sentences (SVO + "and/but"). Rare complex structures.                                            |
| 25–49       | **Developing**   | Almost exclusively simple sentences. Very short utterances.                                                                 |
| 0–24        | **Beginner**     | Fragmented speech. Single words or very short phrases.                                                                      |

**What to flag:** Long stretches of only simple sentences, missed opportunities for subordination, run-on sentences.

**Bonus signals:** Sentence variety in a single response, effective use of transitions (however, therefore, consequently).

---

## 5. Idiom Usage (0–100)

Measures natural use of English idioms, collocations, and figurative language.

| Score Range | Label           | Criteria                                                                      |
| ----------- | --------------- | ----------------------------------------------------------------------------- |
| 90–100      | **Native-like** | Uses idioms naturally and correctly. Varied idioms from different categories. |
| 75–89       | **Strong**      | Uses some idioms correctly. Shows awareness of figurative language.           |
| 50–74       | **Developing**  | Attempts idioms but sometimes uses them incorrectly or in wrong contexts.     |
| 25–49       | **Rare**        | Rarely uses idioms. Speech is mostly literal.                                 |
| 0–24        | **None**        | No idiom usage. Entirely literal speech.                                      |

**What to flag:** Misused idioms (wrong meaning or context), correctly used idioms (positive reinforcement), missed opportunities where an idiom would be natural.

---

## 6. Speaking Pace (0–100)

Measures appropriateness of speaking speed — neither too fast nor too slow.

| Score Range | Label           | Criteria                                                                                            |
| ----------- | --------------- | --------------------------------------------------------------------------------------------------- |
| 90–100      | **Optimal**     | 130–160 WPM. Natural rhythm with purposeful pauses. Speed varies with content (slows for emphasis). |
| 75–89       | **Good**        | 120–170 WPM. Mostly natural pace with minor rushes or hesitations.                                  |
| 50–74       | **Moderate**    | 100–120 or 170–190 WPM. Noticeably slow (searching for words) or fast (nervous rushing).            |
| 25–49       | **Uneven**      | <100 or >190 WPM. Very slow with long pauses or very fast making it hard to follow.                 |
| 0–24        | **Problematic** | Extremely slow (word-by-word) or rapid-fire unintelligible speech.                                  |

**What to flag:** Long pauses (>3 seconds) — could indicate word-finding difficulty. Sudden speed changes. Consistent rushing at end of sentences.

---

## 7. Coherence (0–100)

Measures logical flow, organization of thoughts, use of transitions, and staying on topic.

| Score Range | Label          | Criteria                                                                                                  |
| ----------- | -------------- | --------------------------------------------------------------------------------------------------------- |
| 90–100      | **Excellent**  | Ideas flow logically. Clear structure (intro → detail → conclusion). Natural transitions. Stays on topic. |
| 75–89       | **Good**       | Generally well-organized. Occasional tangent but returns to topic. Some transitions used.                 |
| 50–74       | **Adequate**   | Ideas are understandable but organization is loose. Jumps between points. Few transitions.                |
| 25–49       | **Weak**       | Hard to follow the thread. Jumps topics without connection. No transitions.                               |
| 0–24        | **Incoherent** | No logical structure. Disconnected fragments. Unclear what they're trying to say.                         |

**What to flag:** Topic jumps without transition, circular reasoning, unfinished thoughts, contradictions within the same response.

---

## 8. Confidence (0–100)

Measures perceived confidence through linguistic signals — hedging, volume consistency, commitment to statements.

| Score Range | Label              | Criteria                                                                                                              |
| ----------- | ------------------ | --------------------------------------------------------------------------------------------------------------------- |
| 90–100      | **Very Confident** | Makes clear, direct statements. Commits to opinions. Rarely hedges unnecessarily.                                     |
| 75–89       | **Confident**      | Mostly direct. Occasional hedging but appropriate. Doesn't second-guess excessively.                                  |
| 50–74       | **Moderate**       | Mixes confident and hedging language. Often adds "I think" or "maybe" when unnecessary.                               |
| 25–49       | **Low**            | Frequently hedges, apologizes for opinions, uses excessive qualifiers. "Sorry, I'm not sure if this is right, but..." |
| 0–24        | **Very Low**       | Constantly apologizes. Trails off mid-sentence. Refuses to commit to any statement.                                   |

**What to flag:** Excessive hedging phrases (I think, maybe, sort of, kind of, I guess, I'm not sure), unnecessary apologies, trailing off, upspeak (statement sounds like a question).

**Note:** Some hedging is natural and polite — only flag when excessive or when it undermines an otherwise good point.

---

## Scoring Aggregation

**Overall Score** = Weighted average:

- Grammar: 20%
- Vocabulary: 15%
- Filler Words: 10%
- Sentence Complexity: 10%
- Idiom Usage: 10%
- Speaking Pace: 10%
- Coherence: 15%
- Confidence: 10%

**Letter Grades:**

- 90–100: A+ (Expert)
- 80–89: A (Advanced)
- 70–79: B (Upper Intermediate)
- 60–69: B- (Intermediate)
- 50–59: C (Lower Intermediate)
- 40–49: D (Developing)
- 0–39: F (Beginner)
