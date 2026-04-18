# FluentAI — The AI English Coach That Listens to You Speak and Makes You Dangerously Articulate

> **MLH AI Hackfest** | 1000+ participants | ~20 hours to build
> **Theme:** "AI that thinks/decides better than humans"
> **Target Prizes:** Best Use of ElevenLabs (primary) + Best Use of Gemini API (secondary)
> **Deliverables:** Working demo + 2-min video + public GitHub repo

---

## The One-Liner

**Duolingo is a typing game. FluentAI is a speaking gym.**

You tell it what you want to master — job interviews, public speaking, sales pitches, casual conversation, academic presentations — and it generates a personalized roadmap of voice lessons. Each lesson is a real-time voice call with an AI character who adapts to YOUR level. While you talk, it tracks everything: grammar, vocabulary depth, filler words, idiom usage, sentence complexity, confidence, pacing. After every call, you get a brutal honest report card. Over time, it builds your Speech DNA — a living profile of how you speak — and ensures every single lesson attacks your weakest points.

Nobody else at this hackathon will build a voice-first, gamified, adaptive language coaching platform. Everyone will build chatbots. We build the thing that makes you sound like you went to Oxford.

---

## Why This Wins the Hackathon

### Theme Adherence: "AI that thinks/decides better than humans"

A human English tutor can catch maybe 30% of your mistakes while also managing the conversation, planning the next question, and keeping you engaged. They can't simultaneously track your grammar error rate, count your filler words, measure your sentence complexity, detect missed idiom opportunities, AND steer the conversation toward your weaknesses. FluentAI does ALL of this at once, in real-time, every single call. It literally evaluates your speech better than any human tutor can.

### Originality

- Duolingo = text-based, pre-scripted lessons, no actual speaking practice
- ChatGPT Voice = general-purpose, no curriculum, no progression, no tracking
- Nobody has combined ElevenLabs Conversational AI + Gemini analysis into a structured learning platform with gamification
- The "each lesson is a call" mechanic is genuinely novel

### Demo Factor (2-min video)

The demo IS the product. Judge watches someone:

1. Pick "Job Interviews" → see a personalized roadmap appear
2. Start a lesson → have a real voice conversation with an AI interviewer
3. Make mistakes → see them highlighted LIVE on screen
4. Finish the call → dramatic report card reveal with a score, XP earned, level-up animation
5. See their Speech DNA evolve over time

This is visceral. Judges HEAR the product working.

### Technical Depth

- ElevenLabs: Conversational AI, multiple voice personas, tool calling, knowledge base
- Gemini: Real-time transcript analysis, grammar parsing, idiom detection, report generation, roadmap generation
- Not a wrapper around one API — it's a system where two AI platforms work in concert

---

## Core Product: How It Works

### Step 1: Onboarding — "What Do You Want to Master?"

```
User opens FluentAI → picks a goal:

┌─────────────────────────────────────────┐
│  🎯 What do you want to get better at?  │
│                                         │
│  💼 Job Interviews                      │
│  🎤 Public Speaking                     │
│  💰 Sales & Negotiation                 │
│  🗣  Casual Conversation                │
│  📚 Academic Presentations              │
│  🌍 Business English                    │
│  ✏️  Custom Topic: ____________          │
│                                         │
└─────────────────────────────────────────┘
```

They can also type a completely custom goal: "I want to prepare for my Google PM interview" or "I want to be better at networking events" or "I need to present my thesis defense."

### Step 2: Diagnostic Call — "Let's Hear You Speak"

Before any roadmap is generated, FluentAI runs a **5-minute diagnostic call** — an unstructured conversation to baseline your current level.

```
AI (warm, encouraging voice): "Hey! I'm your coach. Before we build
your training plan, I just want to chat for a few minutes so I can
understand where you're at. No pressure, no scoring — just talk to me.
So, tell me about yourself. What do you do, and why do you want to
improve your English?"

User speaks freely for 5 minutes.

→ FluentAI silently analyzes EVERYTHING:
  - Vocabulary range (unique words / total words)
  - Average sentence length & complexity
  - Grammar error frequency & types
  - Filler word count (um, uh, like, you know, basically)
  - Idiom & phrase usage (or absence)
  - Speaking pace (WPM)
  - Confidence indicators (hedging, uptalk, trailing off)
  - Topic coherence & structure
```

This diagnostic produces the initial **Speech DNA** profile (more on this below).

### Step 3: Roadmap Generation — AI Builds Your Curriculum

Based on the diagnostic + chosen goal, Gemini generates a **personalized roadmap** divided into levels. Each level has 4-6 short lessons. Each lesson is a voice call with a specific objective.

```
📍 YOUR ROADMAP: Job Interview Mastery

LEVEL 1 — Foundations (Beginner) ⬜⬜⬜⬜
  📞 Lesson 1: "Tell Me About Yourself" — structured self-intro
  📞 Lesson 2: "Why This Company?" — research articulation
  📞 Lesson 3: "Strengths & Weaknesses" — honest yet strategic framing
  📞 Lesson 4: "Walk Me Through Your Resume" — chronological storytelling
  🏆 Boss Battle: Full 10-min mock interview (all L1 topics combined)

LEVEL 2 — Intermediate ⬜⬜⬜⬜⬜
  📞 Lesson 5: "Behavioral Questions" — STAR method practice
  📞 Lesson 6: "Technical Explanation" — explain complex ideas simply
  📞 Lesson 7: "Handling Curveballs" — unexpected/tough questions
  📞 Lesson 8: "Salary Negotiation" — confident number conversations
  📞 Lesson 9: "Asking Smart Questions" — flip the interview
  🏆 Boss Battle: Pressure interview (rapid-fire, interruptions, curveballs)

LEVEL 3 — Advanced ⬜⬜⬜⬜
  📞 Lesson 10: "Executive Presence" — authority without arrogance
  📞 Lesson 11: "Storytelling with Data" — weave numbers into narrative
  📞 Lesson 12: "Panel Interview Sim" — multiple personalities
  📞 Lesson 13: "Case Study Walkthrough" — structured problem-solving aloud
  🏆 Boss Battle: 15-min intense VP-level interview with adversarial follow-ups

LEVEL 4 — Expert (Hidden until L3 complete) 🔒
  📞 ...unlocks dynamically based on remaining weaknesses...
```

**Key design:**

- Roadmap is NOT static — it reshuffles based on your Speech DNA after every call
- If you keep making grammar mistakes, new grammar-focused lessons get injected
- If your filler word count drops, those lessons get skipped
- Boss Battles are gatekeepers — you need a minimum score to unlock the next level

### Step 4: The Lesson — A Live Voice Call

This is the core product loop. Each lesson is a **3-7 minute voice call** with an AI character.

**What happens during the call:**

```
┌─────────────────────────────────────────────────────────────────┐
│                        LESSON IN PROGRESS                       │
│                                                                 │
│  ┌──────────────────────┐  ┌──────────────────────────────────┐ │
│  │   AI CHARACTER       │  │   LIVE ANALYSIS SIDEBAR          │ │
│  │                      │  │                                  │ │
│  │   🎭 Sarah Chen      │  │   📊 Live Stats                  │ │
│  │   Senior Recruiter   │  │   Grammar: ✅✅✅❌✅ (80%)      │ │
│  │   @ Google           │  │   Filler Words: 3 (🟡)          │ │
│  │                      │  │   Vocabulary: Level 3 (🟢)      │ │
│  │   [Waveform viz]     │  │   Pace: 142 WPM (🟢)           │ │
│  │                      │  │   Complexity: 6.2/10 (🟡)       │ │
│  │   "Tell me about a   │  │                                  │ │
│  │   time you led a     │  │   ⚡ Live Mistakes               │ │
│  │   project through    │  │   0:42 "more better" → "better"  │ │
│  │   unexpected          │  │   1:15 "I was do" → "I was doing"│ │
│  │   challenges."       │  │   2:01 Used "basically" (filler) │ │
│  │                      │  │                                  │ │
│  └──────────────────────┘  │   💡 Missed Opportunities        │ │
│                            │   1:30 Could've used "spearhead" │ │
│  ┌──────────────────────┐  │       instead of "I led"         │ │
│  │  YOUR TRANSCRIPT     │  │   2:15 Could've used STAR method │ │
│  │  (live, scrolling)   │  │       — you forgot the Result    │ │
│  │                      │  │                                  │ │
│  │  "So I was working   │  └──────────────────────────────────┘ │
│  │   on this project    │                                       │
│  │   and we had to..."  │  [END CALL]  [HINT]  [PAUSE]         │
│  └──────────────────────┘                                       │
└─────────────────────────────────────────────────────────────────┘
```

**The AI character:**

- Has a distinct persona (name, role, personality, voice)
- Is designed to ELICIT specific language patterns from you
- Adapts difficulty mid-call: if you're crushing it, the questions get harder. If you're struggling, it softens
- Uses ElevenLabs Conversational AI with tool calling — every few seconds it calls a backend tool to log your latest metrics
- Has a knowledge base loaded with the lesson objectives, evaluation rubrics, and coaching strategies

**What the AI is tracking (silently, in real-time via tool calls):**

| Dimension             | What's Measured                                         | Example                                                                 |
| --------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------- |
| Grammar Accuracy      | Error count, error types (tense, agreement, articles)   | "I have went" → should be "I have gone"                                 |
| Vocabulary Depth      | Unique words, advanced word usage, repetition           | Using "good" 8 times when "exceptional", "stellar", "commendable" exist |
| Filler Words          | Count of um, uh, like, basically, you know, so, right   | "So, like, basically what happened was, um..."                          |
| Sentence Complexity   | Avg length, subordinate clauses, varied structure       | All simple sentences = low score                                        |
| Idiom & Phrase Usage  | Natural use of English idioms and collocations          | "Hit the ground running", "at the end of the day"                       |
| Speaking Pace         | Words per minute, variation, pauses                     | Too fast (>180 WPM) or too slow (<100 WPM)                              |
| Coherence & Structure | Logical flow, transitions, STAR method usage            | Rambling vs structured response                                         |
| Confidence Signals    | Hedging ("I think maybe"), uptalk, trailing off         | "I'm not sure but maybe I could..." vs "I led the team to..."           |
| Pronunciation Flags   | Commonly mispronounced words (detected from transcript) | "Specific" vs "pacific", "library" vs "libary"                          |
| Topic Adherence       | Staying on-topic vs going on tangents                   | Answering "Tell me about yourself" with a 3-min tangent about your cat  |

### Step 5: The Report Card — Post-Call Breakdown

After every call, the user gets a **detailed, beautiful report card**.

```
┌─────────────────────────────────────────────────────────────────┐
│                     📊 LESSON 5 REPORT CARD                     │
│                     "Behavioral Questions"                      │
│                                                                 │
│              ⭐ OVERALL SCORE: 72/100  (+8 from last)           │
│              🏅 XP EARNED: 340  |  🔥 STREAK: 4 days           │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  DIMENSION BREAKDOWN                                     │   │
│  │                                                          │   │
│  │  Grammar Accuracy    ████████░░  78% (+5%)  🟢           │   │
│  │  Vocabulary Depth    ██████░░░░  62%  (=)   🟡           │   │
│  │  Filler Words        █████████░  12→ 8      🟢           │   │
│  │  Sentence Complexity ███████░░░  68% (+3%)  🟡           │   │
│  │  Idiom Usage         ████░░░░░░  40%  (-2%) 🔴           │   │
│  │  Speaking Pace       ████████░░  145 WPM    🟢           │   │
│  │  Coherence           ████████░░  82% (+10%) 🟢           │   │
│  │  Confidence          ██████░░░░  65% (+4%)  🟡           │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  🎯 KEY MOMENTS                                                 │
│                                                                 │
│  ✅ Great: "I spearheaded the migration to microservices,       │
│     reducing deployment time by 40%." — Strong verb + data!     │
│                                                                 │
│  ❌ Fix: "We was working on..." → "We were working on..."       │
│     (subject-verb agreement — this is your #1 recurring error)  │
│                                                                 │
│  💡 Missed: When describing the challenge, you could have used  │
│     "It was a baptism by fire" — natural idiom for this context │
│                                                                 │
│  ⚡ POWER-UPS UNLOCKED                                          │
│  🔓 "Idiom Injector" — Next lesson will feed you 3 idioms to   │
│     try to naturally weave into conversation                    │
│  🔓 "Ghost Correction" — Next lesson will show real-time        │
│     corrections as you speak                                    │
│                                                                 │
│  📈 YOUR SPEECH DNA UPDATED                                     │
│  Grammar improved → roadmap adjusted (skipping Lesson 7,        │
│  adding "Advanced Vocabulary" lesson instead)                   │
│                                                                 │
│  [REPLAY CALL WITH ANNOTATIONS]  [NEXT LESSON]  [SHARE]        │
└─────────────────────────────────────────────────────────────────┘
```

### Step 6: Speech DNA — Your Living Speaking Profile

This is the "wow feature" that ties it all together. Across every lesson, FluentAI builds a persistent **Speech DNA** profile — a multi-dimensional fingerprint of how you speak English.

```
┌─────────────────────────────────────────────────────────────────┐
│                    🧬 YOUR SPEECH DNA                            │
│                                                                 │
│          Grammar ──── 78%                                       │
│         ╱                  ╲                                    │
│   Confidence              Vocabulary                            │
│      65%                     62%                                │
│       │        ╱ radar ╲      │                                 │
│       │       ╱  chart  ╲     │                                 │
│   Coherence              Complexity                             │
│      82%                     68%                                │
│         ╲                  ╱                                    │
│          Pace ──────── Idioms                                   │
│          85%            40%                                     │
│                                                                 │
│  📊 TRENDS (last 10 lessons)                                    │
│  Grammar:    📈 +15% (was 63%, now 78%) — strong improvement    │
│  Vocabulary: ➡️  stagnant at 62% — needs focused work           │
│  Idioms:     📉 -5% (declined) — adding idiom-focused lessons   │
│  Filler:     📈 22→8 per session — great improvement            │
│                                                                 │
│  🏷 YOUR TAGS                                                    │
│  #GrammarImprover  #FillerWordSlayer  #NeedsIdioms              │
│  #StrongCoherence  #VocabularyPlateau                           │
│                                                                 │
│  🤖 AI INSIGHT                                                   │
│  "You structure your thoughts well and your grammar has improved │
│   dramatically. Your biggest growth opportunity is vocabulary    │
│   diversity — you use 'good', 'great', and 'important' as your  │
│   go-to adjectives. Next 3 lessons will focus on synonym        │
│   richness in professional contexts."                           │
└─────────────────────────────────────────────────────────────────┘
```

**The Speech DNA drives everything:**

- Roadmap reshuffling (inject lessons for weak dimensions)
- Lesson difficulty calibration (AI character adjusts complexity)
- Progress visualization (the radar chart evolves over time)
- "AI Coach Insight" — a Gemini-powered natural language summary of your trajectory

---

## Gamification System

### XP & Leveling

```
Every lesson earns XP based on performance:
- Base XP: 100 per completed lesson
- Grammar bonus: +5 XP per clean sentence (no errors)
- Vocabulary bonus: +10 XP per advanced word used naturally
- Idiom bonus: +25 XP per idiom used correctly
- Zero filler bonus: +50 XP for a lesson with <3 filler words
- Perfect score bonus: +200 XP for 90%+ overall
- Streak multiplier: Day 3+ streak = 1.5x, Day 7+ = 2x

Levels:
Level 1: Beginner (0 - 500 XP) — "Getting Started"
Level 2: Elementary (500 - 1500 XP) — "Finding Your Voice"
Level 3: Intermediate (1500 - 3500 XP) — "Building Confidence"
Level 4: Upper-Intermediate (3500 - 7000 XP) — "Getting Sharp"
Level 5: Advanced (7000 - 12000 XP) — "Commanding Presence"
Level 6: Expert (12000+ XP) — "Dangerously Articulate"
```

### Achievements

```
🏆 First Words       — Complete your first lesson
🏆 Grammar Guardian  — 3 consecutive lessons with 90%+ grammar
🏆 Filler Slayer     — Complete a lesson with 0 filler words
🏆 Idiom Master      — Use 5 different idioms correctly in one lesson
🏆 Speed Demon       — Maintain 140-160 WPM for an entire lesson
🏆 Vocabulary Vault  — Use 50+ unique words in a single lesson
🏆 Boss Slayer       — Pass a Boss Battle on first attempt
🏆 Streak Machine    — 7-day streak
🏆 Polymath          — Complete roadmaps in 3 different topics
🏆 The Articulate    — Reach Level 6 in any topic
```

### Boss Battles

Every level ends with a **Boss Battle** — a longer, harder call that tests everything from that level combined. The AI character becomes tougher: faster questions, interruptions, curveballs, higher expectations.

```
🏆 LEVEL 1 BOSS BATTLE: "The Screening Call"
   Duration: 8 minutes
   Character: Friendly but thorough HR recruiter
   Test: All Level 1 skills combined — self-intro, company knowledge,
         strengths/weaknesses, resume walkthrough
   Pass threshold: 70% overall
   Reward: 500 XP + "Screening Survivor" badge + Level 2 unlock

🏆 LEVEL 2 BOSS BATTLE: "The Pressure Cooker"
   Duration: 10 minutes
   Character: Senior hiring manager, slightly impatient
   Test: Rapid-fire behavioral questions, salary negotiation attempt,
         one deliberate curveball ("Why shouldn't we hire you?")
   Pass threshold: 75% overall
   Reward: 800 XP + "Pressure Proof" badge + Level 3 unlock
```

### Preparation Mode — Pre-Lesson Study

Before each lesson, the user can view **AI-generated preparation material**:

```
📖 PREP FOR LESSON 5: "Behavioral Questions"

🎯 Lesson Objective:
Master the STAR method (Situation, Task, Action, Result) for
behavioral interview questions.

📝 Key Vocabulary to Use:
- "spearheaded" (instead of "led")
- "mitigated" (instead of "reduced" or "fixed")
- "cross-functional" (instead of "different teams")
- "deliverables" (instead of "things we needed to do")
- "iterate" (instead of "try again")

🗣 Phrases to Practice:
- "In that situation, I chose to..."
- "The measurable impact was..."
- "Looking back, I would have also..."

💡 Idioms That Fit This Topic:
- "Hit the ground running" — started contributing immediately
- "Wear many hats" — took on multiple roles
- "Move the needle" — made measurable impact
- "Behind the eight ball" — in a difficult situation

📋 Sample Questions You'll Face:
1. Tell me about a time you led a team through a challenge
2. Describe a situation where you had to make a tough decision quickly
3. Give an example of when you failed and what you learned

⏱ Estimated Call Duration: 5 minutes
```

This is generated by Gemini based on the lesson topic + the user's Speech DNA (it highlights vocabulary and idioms the user is WEAK at specifically).

---

## Call Replay Mode — Annotated Playback

After any lesson, users can replay the call with full annotations overlaid:

```
┌─────────────────────────────────────────────────────────────────┐
│  ▶ REPLAYING LESSON 5  [0:00 ─────●──────────────────── 5:23]  │
│                                                                 │
│  🔊 Playing...                                                  │
│                                                                 │
│  YOU: "So basically um I was working on this project            │
│        ~~~~~~       ~~                                          │
│        filler      filler                                       │
│                                                                 │
│        and we was trying to figure out how to..."               │
│            ~~~                                                   │
│            ❌ "we were trying"                                   │
│                                                                 │
│  GHOST (what you should have said):                             │
│  "I was spearheading a project where our team needed to..."     │
│   ✅ eliminates fillers  ✅ stronger verb  ✅ clearer structure  │
│                                                                 │
│  AI: "That's interesting. What was the biggest challenge?"      │
│                                                                 │
│  YOU: "The biggest challenge was that we had to do a lot of     │
│        things at the same time and it was very hard..."         │
│        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~             │
│        💡 Try: "We were juggling multiple competing priorities  │
│           under a tight deadline, which tested our ability to   │
│           prioritize ruthlessly."                               │
│                                                                 │
│  [◀ PREV MOMENT]  [NEXT MOMENT ▶]  [JUMP TO MISTAKES ONLY]    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Technical Architecture

### System Design

```
┌──────────────────────────────────────────────────────────────────┐
│                         FRONTEND                                  │
│                     Next.js + React                               │
│                                                                   │
│  ┌────────────┐ ┌──────────────┐ ┌─────────────┐ ┌───────────┐  │
│  │ Onboarding │ │ Lesson View  │ │  Report Card│ │ Speech DNA│  │
│  │ + Roadmap  │ │ (Live Call)  │ │  + Replay   │ │ Dashboard │  │
│  └────────────┘ └──────┬───────┘ └─────────────┘ └───────────┘  │
│                        │                                          │
│          ElevenLabs    │  Transcript +                            │
│          React SDK     │  Analysis Stream                        │
│          (voice call)  │  (WebSocket)                            │
└────────────────────────┼──────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│                     ELEVENLABS PLATFORM                           │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  Conversational AI Agent                                   │  │
│  │  - System prompt: persona + lesson objectives + rubric     │  │
│  │  - Voice: distinct per character (recruiter, coach, etc)   │  │
│  │  - Knowledge Base: lesson content, evaluation criteria,    │  │
│  │    idioms database, grammar rules                          │  │
│  │  - Tool Calling → hits our backend every ~15 seconds       │  │
│  │    to log transcript + get live analysis                   │  │
│  └──────────────┬─────────────────────────────────────────────┘  │
│                 │ tool_call: analyze_speech(transcript_chunk)     │
└─────────────────┼────────────────────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────────────────────┐
│                      BACKEND (Python FastAPI)                     │
│                                                                   │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────────┐  │
│  │ Analysis Engine │  │ Roadmap Engine │  │ Gamification Engine│  │
│  │ (Gemini API)   │  │ (Gemini API)   │  │ (XP, levels, etc) │  │
│  │                │  │                │  │                    │  │
│  │ - Grammar check│  │ - Generate     │  │ - Calculate XP     │  │
│  │ - Vocabulary   │  │   curriculum   │  │ - Check achievemts │  │
│  │ - Filler count │  │ - Reshuffle    │  │ - Update streaks   │  │
│  │ - Idiom detect │  │   based on DNA │  │ - Level-ups        │  │
│  │ - Complexity   │  │ - Prep material│  │                    │  │
│  │ - Confidence   │  │   generation   │  │                    │  │
│  │ - Pace calc    │  │                │  │                    │  │
│  └───────┬────────┘  └────────────────┘  └────────────────────┘  │
│          │                                                        │
│          ▼                                                        │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │                    Data Store                              │  │
│  │  - User profiles + Speech DNA (JSON / SQLite)              │  │
│  │  - Lesson history + transcripts                            │  │
│  │  - Roadmap state                                           │  │
│  │  - XP / achievements / streaks                             │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────────────────────┐
│                      GEMINI API                                   │
│                                                                   │
│  Used for:                                                        │
│  1. Real-time transcript analysis (grammar, vocabulary, etc)     │
│  2. Roadmap generation (personalized curriculum)                 │
│  3. Report card generation (natural language insights)           │
│  4. Prep material generation (vocab, phrases, idioms)            │
│  5. Speech DNA insight generation ("Your biggest weakness is..")  │
│  6. Ghost correction generation (what you should have said)      │
│  Model: gemini-2.5-flash (fast, cheap, great for analysis)      │
└──────────────────────────────────────────────────────────────────┘
```

### Data Flow During a Live Lesson

```
1. User speaks into microphone
   │
   ▼
2. ElevenLabs Conversational AI receives audio
   - Transcribes speech (ASR)
   - AI character responds with next question/comment (LLM → TTS)
   - Every ~15 seconds, calls tool: analyze_speech(latest_transcript)
   │
   ▼
3. Backend receives transcript chunk via tool call
   - Sends to Gemini for instant analysis
   - Returns structured analysis to ElevenLabs (so AI can adapt)
   - Pushes analysis to frontend via WebSocket
   │
   ▼
4. Frontend receives live analysis stream
   - Updates sidebar: grammar score, filler count, vocabulary stats
   - Shows mistakes as they happen
   - Shows missed opportunities (better words, idioms)
   │
   ▼
5. Call ends → Backend generates full report
   - Aggregates all chunk analyses
   - Gemini generates: report card, ghost corrections, AI insights
   - Updates Speech DNA
   - Calculates XP, checks achievements, updates roadmap
   - Sends final report to frontend
```

---

## Tech Stack

| Component           | Technology                                         | Why                                                            |
| ------------------- | -------------------------------------------------- | -------------------------------------------------------------- |
| Frontend            | Next.js 14 + TypeScript + Tailwind                 | Fast, SSR for initial load, great DX                           |
| Voice Calls         | ElevenLabs Conversational AI + `@11labs/react` SDK | Real-time voice, tool calling, knowledge base, multiple voices |
| Analysis Engine     | Gemini 2.5 Flash API                               | Fast, cheap, excellent at text analysis tasks                  |
| Backend             | Python FastAPI + WebSocket                         | Async, fast, easy Gemini SDK integration                       |
| Database            | SQLite (via `aiosqlite`)                           | Zero setup, sufficient for hackathon demo                      |
| Gamification        | Custom Python module                               | XP calc, achievement checking, level logic                     |
| Deployment          | Vercel (frontend) + Railway/Render (backend)       | Free tier, fast deploys                                        |
| Audio Visualization | Web Audio API + Canvas                             | Waveform display during calls                                  |
| Charts              | Recharts                                           | Radar chart for Speech DNA, bar charts for reports             |
| Animation           | Framer Motion                                      | Level-up animations, score reveals                             |

---

## ElevenLabs Integration (Deep)

### Agent Configuration

```
Agent: FluentAI Coach
├── System Prompt: Dynamic (changes per lesson)
│   "You are Sarah Chen, a senior recruiter at Google conducting
│    a behavioral interview. Your job is to ask questions that
│    elicit STAR-method responses. Evaluate the user's speaking
│    quality. If they struggle, gently rephrase your question.
│    If they're doing well, ask harder follow-ups. Never break
│    character. Call analyze_speech every 15 seconds."
│
├── Voice: "Rachel" for coach, "Josh" for recruiter, "Bella" for
│          casual friend, "Adam" for tough interviewer
│
├── Knowledge Base:
│   ├── grammar_rules.md — Top 50 English grammar rules + examples
│   ├── idioms_database.md — 200 common English idioms by topic
│   ├── interview_rubric.md — How to assess interview performance
│   ├── lesson_objectives.md — Per-lesson goals and evaluation criteria
│   └── coaching_strategies.md — How to adapt difficulty, encourage, push
│
├── Tools (function calling):
│   ├── analyze_speech(transcript: str) → AnalysisResult
│   │   Called every ~15 seconds during lesson
│   │   Backend sends transcript to Gemini, returns scores
│   │   ElevenLabs agent uses result to adapt next response
│   │
│   ├── get_lesson_context() → LessonInfo
│   │   Returns current lesson objectives, user's weaknesses,
│   │   target vocabulary/idioms to elicit
│   │
│   └── end_lesson(final_transcript: str) → void
│       Called when conversation naturally wraps up
│       Triggers full report generation
│
└── Settings:
    ├── Turn detection: Server-managed (avoids premature cutoffs)
    ├── Max duration: 10 minutes (auto-end with graceful wrap-up)
    └── Silence detection: After 10s silence, coach prompts user
```

### Multiple Voice Personas

Each lesson type uses a different ElevenLabs voice to create distinct characters:

| Character       | Voice                          | Personality                      | Used For                          |
| --------------- | ------------------------------ | -------------------------------- | --------------------------------- |
| Coach Alex      | "Kore" / warm male             | Encouraging, patient, analytical | Diagnostic call, coaching moments |
| Sarah Chen (HR) | "Rachel" / professional female | Friendly but structured          | Interview screening lessons       |
| David Park (VP) | "Adam" / authoritative male    | Direct, high expectations        | Advanced/boss battle interviews   |
| Maya (Friend)   | "Bella" / casual female        | Relaxed, natural                 | Casual conversation lessons       |
| Prof. Williams  | "Josh" / distinguished male    | Academic, articulate             | Presentation/academic lessons     |

---

## Gemini Integration (Deep)

### Analysis Prompt (called every ~15 seconds during a call)

```python
ANALYSIS_PROMPT = """
You are an expert English language analyst. Analyze this transcript chunk
from a non-native or developing English speaker. Return a JSON analysis.

TRANSCRIPT CHUNK:
{transcript}

USER'S CURRENT SPEECH DNA:
{speech_dna}

LESSON OBJECTIVE:
{lesson_objective}

Analyze and return this exact JSON structure:
{
  "grammar": {
    "score": 0-100,
    "errors": [
      {"text": "what they said", "correction": "what they should say",
       "rule": "subject-verb agreement", "timestamp_approx": "1:23"}
    ]
  },
  "vocabulary": {
    "score": 0-100,
    "unique_words": 45,
    "advanced_words_used": ["spearheaded", "mitigated"],
    "missed_opportunities": [
      {"used": "very important", "better": "critical/paramount/pivotal"}
    ]
  },
  "filler_words": {
    "count": 3,
    "instances": ["um (0:15)", "basically (0:42)", "like (1:01)"]
  },
  "idioms": {
    "used_correctly": ["hit the ground running"],
    "missed_opportunities": [
      {"context": "describing a difficult start", "idiom": "baptism by fire",
       "example": "It was a real baptism by fire — I had to learn on the fly."}
    ]
  },
  "sentence_complexity": {
    "score": 0-100,
    "avg_words_per_sentence": 12.5,
    "has_subordinate_clauses": true,
    "variation": "moderate"
  },
  "confidence": {
    "score": 0-100,
    "hedging_instances": ["I think maybe", "I'm not sure but"],
    "strong_statements": ["I led the team", "We achieved 40% improvement"]
  },
  "pace_wpm": 142,
  "coherence": {
    "score": 0-100,
    "note": "Good STAR structure but forgot the Result component"
  },
  "ghost_correction": "Here's how an expert would have expressed the same ideas: ..."
}
"""
```

### Roadmap Generation Prompt

```python
ROADMAP_PROMPT = """
You are an expert English fluency curriculum designer. Based on the user's
diagnostic Speech DNA and their chosen goal, generate a personalized
learning roadmap.

USER'S SPEECH DNA (from diagnostic call):
{speech_dna}

USER'S GOAL: {goal}
(e.g., "Job Interviews", "Public Speaking", "Sales & Negotiation")

Generate a roadmap with 3-4 levels, each containing 4-6 lessons + 1 boss battle.
Each lesson must:
1. Target specific dimensions from the Speech DNA that need improvement
2. Use a scenario that naturally elicits the target language
3. Have a distinct AI character with a name and personality
4. List specific vocabulary and idioms the user should try to use
5. Have clear pass/fail criteria

Return as structured JSON:
{
  "levels": [
    {
      "name": "Foundations",
      "difficulty": "beginner",
      "lessons": [
        {
          "id": 1,
          "title": "Tell Me About Yourself",
          "description": "Practice a structured self-introduction",
          "character": {"name": "Sarah Chen", "role": "HR Recruiter", "voice": "rachel"},
          "target_dimensions": ["coherence", "confidence"],
          "target_vocabulary": ["spearheaded", "pivotal", ...],
          "target_idioms": ["hit the ground running", ...],
          "duration_minutes": 5,
          "pass_threshold": 65
        },
        ...
      ],
      "boss_battle": { ... }
    }
  ]
}
"""
```

---

## Project File Structure

```
fluentai/
├── frontend/
│   ├── app/
│   │   ├── page.tsx                  # Landing / topic selection
│   │   ├── layout.tsx                # Root layout with nav
│   │   ├── globals.css               # Tailwind + custom styles
│   │   ├── diagnostic/
│   │   │   └── page.tsx              # Diagnostic call page
│   │   ├── roadmap/
│   │   │   └── page.tsx              # Roadmap view
│   │   ├── lesson/
│   │   │   └── [id]/
│   │   │       └── page.tsx          # Live lesson + analysis sidebar
│   │   ├── report/
│   │   │   └── [id]/
│   │   │       └── page.tsx          # Post-call report card
│   │   ├── replay/
│   │   │   └── [id]/
│   │   │       └── page.tsx          # Annotated call replay
│   │   ├── profile/
│   │   │   └── page.tsx              # Speech DNA + achievements
│   │   └── prep/
│   │       └── [id]/
│   │           └── page.tsx          # Pre-lesson study material
│   ├── components/
│   │   ├── VoiceCall.tsx             # ElevenLabs React SDK wrapper
│   │   ├── LiveAnalysisSidebar.tsx   # Real-time stats during call
│   │   ├── TranscriptView.tsx        # Scrolling transcript with highlights
│   │   ├── ReportCard.tsx            # Post-lesson report
│   │   ├── SpeechDNARadar.tsx        # Radar chart component
│   │   ├── RoadmapView.tsx           # Level/lesson tree
│   │   ├── AchievementPopup.tsx      # XP + achievement animations
│   │   ├── LevelUpAnimation.tsx      # Level-up celebration
│   │   ├── PrepMaterial.tsx          # Pre-lesson study cards
│   │   ├── GhostCorrection.tsx       # "What you should have said"
│   │   ├── WaveformVisualizer.tsx    # Audio waveform during call
│   │   └── ProgressBar.tsx           # XP bar, lesson progress
│   ├── lib/
│   │   ├── api.ts                    # Backend API client
│   │   ├── websocket.ts             # WebSocket for live analysis stream
│   │   ├── elevenlabs.ts            # ElevenLabs config + helpers
│   │   └── types.ts                 # TypeScript types
│   ├── package.json
│   └── next.config.js
│
├── backend/
│   ├── main.py                       # FastAPI app + WebSocket + routes
│   ├── routers/
│   │   ├── lessons.py                # Lesson CRUD + start/end
│   │   ├── analysis.py               # ElevenLabs tool call endpoint
│   │   ├── roadmap.py                # Roadmap generation + reshuffling
│   │   └── profile.py                # Speech DNA + achievements + XP
│   ├── services/
│   │   ├── gemini_analyzer.py        # Gemini-powered speech analysis
│   │   ├── roadmap_generator.py      # Curriculum generation
│   │   ├── report_generator.py       # Post-call report builder
│   │   ├── speech_dna.py             # DNA profile computation + updates
│   │   ├── gamification.py           # XP, levels, achievements, streaks
│   │   └── prep_generator.py         # Pre-lesson material generation
│   ├── models/
│   │   ├── user.py                   # User model
│   │   ├── lesson.py                 # Lesson model
│   │   ├── speech_dna.py             # Speech DNA model
│   │   └── roadmap.py                # Roadmap model
│   ├── elevenlabs_config/
│   │   ├── personas.py               # Character definitions + prompts
│   │   └── knowledge_base/
│   │       ├── grammar_rules.md
│   │       ├── idioms_database.md
│   │       ├── coaching_strategies.md
│   │       └── evaluation_rubrics.md
│   ├── database.py                   # SQLite setup
│   ├── requirements.txt
│   └── .env
│
├── README.md
├── .gitignore
└── demo/
    └── architecture.png
```

---

## Hour-by-Hour Build Plan (~20 hours)

### Phase 1: Foundation (Hours 0-3)

**Hour 0-1: Project Bootstrap**

- `npx create-next-app@latest fluentai --typescript --tailwind`
- Python FastAPI backend with WebSocket support
- SQLite database schema (users, lessons, speech_dna, achievements)
- Environment variables (.env for Gemini key, ElevenLabs key)
- Basic project structure created
- Verify both API keys work with hello-world calls

**Hours 1-3: ElevenLabs Agent Setup**

- Create conversational AI agent on ElevenLabs platform
- Configure first persona (Coach Alex for diagnostic)
- Set up knowledge base (upload grammar rules, idioms database, coaching strategies)
- Implement tool calling endpoint in FastAPI (`POST /api/tools/analyze_speech`)
- Test: Have a basic voice conversation with the agent and see tool calls arrive at backend
- Set up `@11labs/react` SDK in frontend

### Phase 2: Core Loop (Hours 3-10)

**Hours 3-5: Live Analysis Engine**

- Implement Gemini analysis service (`gemini_analyzer.py`)
- Prompt engineering for transcript analysis (grammar, vocabulary, fillers, idioms, etc.)
- Test: Send sample transcript chunks → get structured JSON analysis back
- WebSocket endpoint for streaming analysis to frontend
- Frontend: Build `LiveAnalysisSidebar` component — real-time stats updating during call

**Hours 5-7: Lesson View (The Core Screen)**

- Frontend: Build full lesson view with:
  - Voice call area (ElevenLabs React SDK)
  - Live analysis sidebar (connected to WebSocket)
  - Scrolling transcript with error highlights
  - Timer + lesson info header
- Backend: Lesson session management (start, track, end)
- Test: Do a full lesson call — talk, see live analysis, end call

**Hours 7-9: Report Card Generation**

- Backend: `report_generator.py` — aggregate chunk analyses into final report
- Gemini prompt for generating natural language insights + ghost corrections
- Frontend: Build `ReportCard` component with:
  - Overall score + XP earned
  - Dimension breakdown bars
  - Key moments (great + fix + missed)
  - Ghost corrections
- Animation: Score reveal animation (Framer Motion)
- Test: Complete a lesson → see beautiful report card

**Hour 9-10: Speech DNA**

- Backend: `speech_dna.py` — compute + update DNA from lesson history
- Frontend: `SpeechDNARadar` component — radar chart (Recharts)
- Trend tracking across lessons
- AI insight generation (Gemini writes a paragraph about your trajectory)
- Test: Do 2 lessons → see DNA update between them

### Phase 3: Progression System (Hours 10-14)

**Hours 10-11: Gamification Engine**

- Backend: `gamification.py` — XP calculation, level-ups, achievement checking, streaks
- Frontend: XP bar, level display, achievement popup animations
- Test: Complete a lesson → see XP animate, potentially level up

**Hours 11-13: Roadmap System**

- Backend: `roadmap_generator.py` — Gemini generates personalized curriculum
- Frontend: `RoadmapView` — visual level/lesson tree
- Onboarding flow: topic selection → diagnostic call → roadmap appears
- Roadmap reshuffling logic (after each lesson, DNA-based adjustments)
- Multiple personas configured in ElevenLabs (at least 3 distinct characters)
- Test: Pick "Job Interviews" → do diagnostic → see personalized roadmap

**Hours 13-14: Preparation Mode**

- Backend: `prep_generator.py` — Gemini generates pre-lesson study material
- Frontend: `PrepMaterial` — vocabulary cards, phrases, idioms, sample questions
- Link prep material to each lesson in the roadmap
- Test: Click on upcoming lesson → see useful prep material

### Phase 4: Polish & Demo (Hours 14-20)

**Hours 14-16: UI/UX Polish**

- Landing page with compelling copy and demo screenshot
- Consistent color scheme, typography, spacing
- Dark theme (looks better in demos)
- Level-up animations, achievement popups, score reveals
- Loading states, empty states, error states
- Mobile-responsive layout
- Add Framer Motion transitions between pages

**Hours 16-17: Call Replay (Stretch Feature)**

- Backend: Store full transcript with timestamps + analysis annotations
- Frontend: `Replay` component — playback with highlighted mistakes + ghost corrections
- If time is short, skip this — report card is enough

**Hours 17-18: End-to-End Testing**

- Full demo flow: Onboarding → Diagnostic → Roadmap → Prep → Lesson → Report → DNA
- Fix any broken transitions
- Test with 3 different topic choices
- Prepare compelling demo scenarios

**Hours 18-19: Demo Video (2 minutes)**

```
0:00-0:10  "Meet FluentAI. The AI speaking coach that makes you
            dangerously articulate."
0:10-0:20  Show topic selection → pick "Job Interviews"
0:20-0:40  Diagnostic call — talk for 15 seconds, show live analysis appearing
0:40-0:50  Roadmap generated — personalized for the user
0:50-1:00  Pre-lesson prep material
1:00-1:30  Live lesson: user answers "Tell me about yourself" — show mistakes
           appearing in real-time on sidebar, ghost corrections
1:30-1:50  Report card reveal — score animation, XP earned, achievement unlocked
1:50-2:00  Speech DNA radar chart + "Your roadmap has been adjusted" +
           tech stack diagram flash + CTA
```

**Hours 19-20: Submission**

- Write README (problem, solution, how it works, tech stack, architecture diagram)
- Add screenshots/GIFs to README
- Push to public GitHub repo
- Submit on Devpost with video + repo link
- Write compelling submission description

---

## Pre-Hackathon Setup Checklist

- [ ] ElevenLabs account + API key (Conversational AI access)
- [ ] Google AI Studio API key (Gemini 2.5 Flash access)
- [ ] Create ElevenLabs agent with first persona (Coach Alex)
- [ ] Upload knowledge base files to ElevenLabs (grammar rules, idioms, coaching strategies)
- [ ] Test ElevenLabs Conversational AI with React SDK (basic call works)
- [ ] Test Gemini API with analysis prompt (JSON response parses correctly)
- [ ] Prepare content files:
  - [ ] `grammar_rules.md` — Top 50 rules with examples
  - [ ] `idioms_database.md` — 200 idioms by topic category
  - [ ] `evaluation_rubrics.md` — Scoring criteria per dimension
  - [ ] `coaching_strategies.md` — How to adapt, encourage, push
- [ ] Set up GitHub repo with Next.js + Python FastAPI template
- [ ] Install dependencies: `@11labs/react`, `google-genai`, `fastapi`, `aiosqlite`, `recharts`, `framer-motion`
- [ ] Prepare 3 demo scenarios with good talking points

---

## Risk Mitigation

| Risk                                       | Impact               | Mitigation                                                                                                                                                                         |
| ------------------------------------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ElevenLabs tool calling is slow/unreliable | Live analysis delays | Buffer chunks, analyze in batches of 30s instead of 15s. Fallback: analyze only at end of call                                                                                     |
| Gemini analysis returns inconsistent JSON  | Frontend breaks      | Strict JSON schema validation + fallback defaults for any missing field                                                                                                            |
| ElevenLabs conversation quality is awkward | Bad demo             | Pre-test extensively, tune system prompt until it feels natural. Have a rehearsed demo scenario to demonstrate                                                                     |
| Not enough time for full roadmap system    | Missing progression  | MVP: hardcode one roadmap for "Job Interviews" instead of generating dynamically. Still shows the concept                                                                          |
| Voice quality/latency issues during demo   | Janky demo           | Record demo video with good internet. Live demo backup if video fails                                                                                                              |
| Gamification feels tacked on               | Judges unimpressed   | Make XP/level-up the FIRST thing shown after a lesson. Make the animation satisfying and impossible to miss                                                                        |
| 20h isn't enough for everything            | Incomplete           | Priority cut list (bottom = cut first): Replay → Prep material → Roadmap reshuffling → Dynamic roadmap gen → Multiple personas. Core = one lesson flow with analysis + report card |

---

## Priority Stack (What to Cut If Behind Schedule)

**Must Have (without this, the project doesn't work):**

1. Voice call with ElevenLabs agent (one persona is fine)
2. Live analysis sidebar during call (even basic — grammar + fillers)
3. Post-call report card with scores
4. Basic gamification (XP + level display)

**Should Have (makes it impressive):** 5. Speech DNA radar chart 6. Roadmap view (even if hardcoded) 7. Multiple personas 8. Preparation material

**Nice To Have (makes it mindblowing):** 9. Dynamic roadmap generation (Gemini) 10. Roadmap reshuffling based on DNA 11. Annotated replay mode 12. Achievement system with animations 13. Boss Battles

---

## Competitive Advantage: Why This Wins Over 1000+ Teams

1. **Product, not a feature.** Most hackathon projects are one-trick demos. This is a complete product loop: onboard → diagnose → plan → practice → analyze → improve → repeat.

2. **The demo sells itself.** A judge watches someone TALK to the AI, sees mistakes appear IN REAL TIME, then gets a beautiful report card with a score. There's no "imagine if..." — it works, live, with real speech.

3. **Deep API integration.** ElevenLabs: conversational AI + tool calling + knowledge base + multiple voices. Gemini: analysis + roadmap generation + report generation + prep material. This isn't a thin wrapper.

4. **The gamification is addictive.** XP, levels, streaks, achievements, boss battles — judges will immediately understand the retention loop.

5. **It attacks a real problem.** 1.5 billion English learners worldwide. Duolingo barely touches speaking. Human tutors cost $30-80/hour. This is the gap.

6. **The Speech DNA is memorable.** Judges will remember the radar chart. It's visual, it's personal, it's the kind of feature that makes people say "I want to see MY chart."

---

## 🔥 JUDGE-SHOCKING UPGRADES — Where We Go From Good to Unforgettable

These are the ideas that transform FluentAI from "great hackathon project" to "how did they build this in 20 hours." Each one is ranked by impact and feasibility.

---

### Upgrade 1: Multi-Agent Orchestration Architecture (HIGH IMPACT, MEDIUM EFFORT)

**The Problem With the Current Plan:**
The backend is a monolith — one FastAPI server doing analysis, roadmap gen, gamification, report gen. This works but it doesn't impress technically. Multi-agent is THE buzzword in AI right now and judges will specifically look for it.

**The Upgrade:**
Replace the monolithic analysis pipeline with a **multi-agent system** where specialized AI agents collaborate in real-time during a lesson:

```
┌──────────────────────────────────────────────────────────────────┐
│                    MULTI-AGENT ORCHESTRATOR                       │
│              (Event-driven message bus / asyncio)                 │
│                                                                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │  CONVERSATION    │  │  ANALYZER AGENT │  │  COACH AGENT    │  │
│  │  AGENT           │  │  (Gemini)       │  │  (Gemini)       │  │
│  │  (ElevenLabs)    │  │                 │  │                 │  │
│  │                  │  │  Receives every  │  │  Watches the    │  │
│  │  Runs the live   │  │  transcript     │  │  analyzer's     │  │
│  │  voice call.     │  │  chunk. Returns │  │  output. Decides│  │
│  │  Stays in        │  │  grammar, vocab,│  │  whether to make│  │
│  │  character as    │  │  filler, idiom  │  │  the next Q     │  │
│  │  the interviewer │  │  scores. Detects│  │  harder/easier. │  │
│  │  or conversation │  │  patterns across│  │  Suggests topic │  │
│  │  partner.        │  │  the full       │  │  pivots to hit  │  │
│  │                  │  │  session.       │  │  weak areas.    │  │
│  └────────┬─────────┘  └───────┬─────────┘  └───────┬─────────┘  │
│           │                    │                     │            │
│           ▼                    ▼                     ▼            │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                    EVENT BUS (Redis/In-Memory)               │ │
│  │  Events: transcript_chunk, analysis_result, difficulty_adj,  │ │
│  │  lesson_end, dna_update, xp_earned, achievement_unlocked    │ │
│  └──────────────────────────────────────────────────────────────┘ │
│           │                    │                     │            │
│           ▼                    ▼                     ▼            │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │  DNA AGENT       │  │  GAMIFICATION   │  │  REPORT AGENT   │  │
│  │  (Gemini)        │  │  AGENT          │  │  (Gemini)       │  │
│  │                  │  │  (Python logic) │  │                 │  │
│  │  Continuously    │  │                 │  │  Listens for    │  │
│  │  updates the     │  │  Listens for    │  │  lesson_end     │  │
│  │  Speech DNA      │  │  analysis events│  │  event. Collects│  │
│  │  profile as new  │  │  Calculates XP  │  │  all analysis   │  │
│  │  analysis comes  │  │  in real-time.  │  │  data. Generates│  │
│  │  in. Detects     │  │  Fires          │  │  comprehensive  │  │
│  │  trends mid-     │  │  achievement_   │  │  report card +  │  │
│  │  session.        │  │  unlocked when  │  │  ghost correct- │  │
│  │                  │  │  criteria met.  │  │  ions + insights│  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

**Why judges will love this:**

- "We built a multi-agent system where 6 specialized AI agents collaborate in real-time during every voice call" is a sentence that wins hackathons
- Each agent has a clear single responsibility — this is legit software architecture
- The event bus means agents are decoupled, can be added/removed, and operate asynchronously
- When a judge asks "tell me about your architecture" you pull up this diagram and they're done

**Implementation:** Use Python `asyncio` with an in-memory event bus (just a dict of event queues). Each agent is an async class that subscribes to events and publishes results. No Redis needed for the hackathon — keep it simple.

```python
class AgentOrchestrator:
    """Multi-agent event bus for real-time lesson coordination."""

    def __init__(self):
        self.agents = {}
        self.event_queue = asyncio.Queue()

    async def publish(self, event_type: str, data: dict):
        for agent in self.agents.values():
            if event_type in agent.subscriptions:
                await agent.handle(event_type, data)

    async def register(self, agent: BaseAgent):
        self.agents[agent.name] = agent

class AnalyzerAgent(BaseAgent):
    subscriptions = ["transcript_chunk"]

    async def handle(self, event_type, data):
        analysis = await gemini_analyze(data["transcript"])
        await self.orchestrator.publish("analysis_result", analysis)

class CoachAgent(BaseAgent):
    subscriptions = ["analysis_result"]

    async def handle(self, event_type, data):
        if data["grammar"]["score"] < 50:
            await self.orchestrator.publish("difficulty_adj", {"direction": "easier"})
        elif data["grammar"]["score"] > 85:
            await self.orchestrator.publish("difficulty_adj", {"direction": "harder"})
```

---

### Upgrade 2: "Future You" Voice Clone — The Demo Gasp Moment (HIGHEST IMPACT, LOW EFFORT)

**The Idea:**
At the end of every lesson report card, after showing all the mistakes and ghost corrections, FluentAI plays a **30-second audio clip of "Future You"** — the user's OWN VOICE, cloned via ElevenLabs, speaking the ghost-corrected version of their worst moment perfectly.

```
┌─────────────────────────────────────────────────────────────────┐
│  🔮 HEAR YOUR FUTURE SELF                                       │
│                                                                 │
│  What you said:                                                  │
│  "So basically um I was working on this project and we was       │
│   trying to, like, figure out how to make it more better..."    │
│                                                                 │
│  What Future You sounds like:                                    │
│  ▶ [════════●══════════════] 0:12 / 0:28                        │
│  "I spearheaded a cross-functional initiative where our team    │
│   needed to rapidly iterate on our deployment pipeline.         │
│   Despite tight deadlines, we managed to reduce deployment      │
│   time by 40% — it was a real baptism by fire."                 │
│                                                                 │
│  🎯 Same ideas. Same voice. Expert delivery.                    │
│  This is what you'll sound like after Level 3.                  │
└─────────────────────────────────────────────────────────────────┘
```

**Why this is a judge-killer:**

- The user literally hears THEMSELVES speaking perfectly — this is emotional, visceral, unforgettable
- It uses ElevenLabs' most impressive capability (voice cloning) that no other team will think to use this way
- It transforms the report card from "here's your score" to "here's your future" — incredibly motivating
- Takes maybe 30 minutes to implement (ElevenLabs voice clone API + TTS with cloned voice)

**Implementation:**

- During diagnostic call, capture ~30 seconds of clean user audio for voice cloning
- Use ElevenLabs Instant Voice Clone API to create a voice profile
- After each lesson, generate "Future You" audio: take the ghost correction text, run it through TTS with the cloned voice
- Play it at the end of the report card as the final reveal

**ElevenLabs API flow:**

```python
# 1. Clone voice from diagnostic audio
voice = elevenlabs.clone(
    name="user_voice",
    files=[diagnostic_audio_clip]  # 30s of clean speech
)

# 2. After lesson, generate "Future You" clip
future_audio = elevenlabs.generate(
    text=ghost_correction_text,
    voice=voice,
    model="eleven_multilingual_v2"
)

# 3. Serve to frontend in report card
```

---

### Upgrade 3: Real-Time "Ghost Whisper" Coach Mode (HIGH IMPACT, MEDIUM EFFORT)

**The Idea:**
An optional mode (toggled on/off) where a **second AI agent whispers coaching suggestions** in the user's ear DURING the conversation via a separate audio channel. Like having a debate coach feeding you lines through an earpiece.

```
┌─────────────────────────────────────────────────────────────────┐
│  LESSON IN PROGRESS — 🎧 Ghost Coach: ON                        │
│                                                                 │
│  AI Interviewer: "Tell me about a time you led a project        │
│                   through unexpected challenges."               │
│                                                                 │
│  YOU (speaking): "So I was working on this project and—"        │
│                                                                 │
│  👻 Ghost whispers in your ear (low volume, fast):              │
│     "Try: 'I spearheaded an initiative where...' — use the      │
│      STAR method, start with Situation"                          │
│                                                                 │
│  YOU (adjusts): "I spearheaded a project at my previous         │
│                  company where we faced an unexpected..."        │
│                                                                 │
│  👻 Ghost: "Good! Now add a specific metric."                    │
│                                                                 │
│  [Toggle: 👻 Ghost Coach ON/OFF]                                │
└─────────────────────────────────────────────────────────────────┘
```

**Implementation:**

- Use the Web Audio API to create two audio channels: one for the main AI voice, one for the ghost coach
- The ghost coach is a lightweight Gemini agent that receives real-time transcript + analysis, generates short coaching tips
- Tips are converted to speech via ElevenLabs TTS (different voice, lower volume, faster speed)
- Ghost coach only speaks during pauses (detects silence > 1.5s) so it doesn't overlap

**Why it shocks judges:** Nobody has built a real-time AI coaching earpiece for a hackathon. This is Iron Man-level UI. The demo practically sells itself — judge watches someone get real-time whispered coaching and visibly improve mid-conversation.

---

### Upgrade 4: Gemini Multimodal — Presentation Mode With Slides (HIGH IMPACT, MEDIUM EFFORT)

**The Idea:**
For "Public Speaking" and "Academic Presentations" goals, the user uploads their slide deck (PDF/images). During the lesson, Gemini can SEE the current slide while analyzing the user's speech. The AI knows if you're explaining Slide 3 poorly or spending too long on Slide 7.

```
┌─────────────────────────────────────────────────────────────────┐
│  PRESENTATION MODE — Lesson 8: "Thesis Defense Practice"        │
│                                                                 │
│  ┌──────────────────────┐  ┌──────────────────────────────────┐ │
│  │                      │  │   📊 SLIDE ANALYSIS              │ │
│  │   [Your Slide 3/12]  │  │                                  │ │
│  │   "Market Analysis"  │  │   ⏱ Time on this slide: 2:15    │ │
│  │                      │  │   (🟡 recommended: 1:00-1:30)    │ │
│  │   [slide preview]    │  │                                  │ │
│  │                      │  │   📝 Slide Coverage:              │ │
│  │                      │  │   ✅ Market size mentioned        │ │
│  │                      │  │   ✅ Competitor analysis          │ │
│  │                      │  │   ❌ TAM/SAM/SOM not addressed    │ │
│  │                      │  │   ❌ Growth projections skipped   │ │
│  │   [← Prev] [Next →]  │  │                                  │ │
│  └──────────────────────┘  │   💡 "You mentioned market size  │ │
│                            │   but didn't reference the chart  │ │
│                            │   on your slide. Point to the     │ │
│                            │   data — it strengthens your      │ │
│                            │   argument."                      │ │
│                            └──────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

**Why this shocks judges:**

- Uses Gemini's multimodal capability (vision + text) that most teams won't touch
- Solves a REAL problem — presentation practice is universally needed
- Adds a visual element to the demo that makes it more engaging
- "Our AI can see your slides while you present and tell you if you missed a key point" is a showstopper line

**Implementation:**

```python
# Upload slides → convert to images → Gemini analyzes slide content
# During lesson, Gemini receives: transcript + current slide image

PRESENTATION_ANALYSIS_PROMPT = """
You are analyzing a user's presentation practice. You can see their current slide
and hear what they're saying (via transcript).

CURRENT SLIDE: [image attached]
TRANSCRIPT OF WHAT THEY SAID ABOUT THIS SLIDE: {transcript_chunk}

Analyze:
1. Did they cover all key points visible on the slide?
2. Are they spending too much/little time on this slide?
3. Does their verbal explanation match the visual data?
4. Suggestions for stronger delivery of THIS specific slide's content.
"""
```

---

### Upgrade 5: Adversarial "Pressure Mode" — AI That Fights Back (MEDIUM IMPACT, LOW EFFORT)

**The Idea:**
Beyond cooperative conversations, add a **Pressure Mode** where the AI deliberately:

- Interrupts you mid-sentence
- Asks aggressive follow-up questions
- Challenges your statements ("I don't buy that. Convince me.")
- Creates awkward silences to see how you handle them
- Plays devil's advocate on every point

This is already partially in "Boss Battles" but it should be a distinct, marketable mode.

```
🔴 PRESSURE MODE ACTIVATED — "The Shark Tank"

AI (cutting you off): "Wait, stop. You just said your team 'collaborated
well.' That's a meaningless platitude. Give me a specific example with
a number attached. You have 30 seconds."

[Timer: 00:30 counting down]

AI: "...15 seconds."

AI: "Time. You used 4 filler words in that response. In a real boardroom,
you'd have lost the room. Let's try again. Same question. Zero fillers
this time. Go."
```

**Why this is a demo weapon:**

- Every hackathon project is a friendly chatbot. A deliberately adversarial AI is memorable
- Shows the system's range — it can be encouraging OR ruthless
- "Shark Tank mode" is an instant hook in the demo video
- Requires almost no new code — just a different system prompt for the ElevenLabs agent

---

### Upgrade 6: Audio-Level Analysis — Beyond Transcript (MEDIUM IMPACT, MEDIUM EFFORT)

**The Problem:**
The current plan only analyzes the TEXT transcript. But the raw audio contains critical information the transcript misses:

- Voice confidence (volume, pitch stability)
- Hesitation patterns (micro-pauses before difficult words)
- Speaking rhythm/cadence variation
- Pronunciation quality (not detectable from transcript)
- Emotional tone (nervous, confident, monotone, engaging)

**The Upgrade:**
Use the **Web Audio API** on the frontend to extract audio features in real-time and send them alongside the transcript to the Analyzer Agent:

```javascript
// Frontend: Extract audio features during call
const audioContext = new AudioContext();
const analyser = audioContext.createAnalyser();

function extractFeatures() {
  const dataArray = new Uint8Array(analyser.frequencyBinCount);
  analyser.getByteFrequencyData(dataArray);

  return {
    volume: calculateRMS(dataArray), // Speaking volume
    pitchVariation: calculatePitchRange(), // Monotone vs expressive
    pausePattern: detectPauses(), // Hesitation mapping
    speakingRate: calculateLocalWPM(), // Pace variation within response
  };
}

// Send audio features + transcript to backend every 5 seconds
ws.send(JSON.stringify({ transcript, audioFeatures }));
```

**New Speech DNA dimensions from audio:**

| Dimension        | Source | What it Shows                                          |
| ---------------- | ------ | ------------------------------------------------------ |
| Vocal Confidence | Audio  | Volume consistency, pitch stability, no trailing off   |
| Expressiveness   | Audio  | Pitch variation — monotone vs engaging delivery        |
| Hesitation Map   | Audio  | Micro-pauses before difficult words reveal insecurity  |
| Pronunciation    | Audio  | Compare spectral features to reference pronunciations  |
| Rhythm & Cadence | Audio  | Professional speakers vary pace; amateurs are monotone |

**Why judges care:** "We don't just analyze what you say — we analyze HOW you say it" is a line that separates FluentAI from everything else.

---

### Upgrade 7: Social/Competitive Features — "Speech Battles" (STRETCH, HIGH IMPACT)

**The Idea:**
Two users enter a lesson simultaneously and get scored head-to-head. After 5 minutes each, the AI declares a winner based on Speech DNA scores.

```
🆚 SPEECH BATTLE — "The Elevator Pitch"

┌──────────────────┐    VS    ┌──────────────────┐
│  Player 1: You   │         │  Player 2: Maya   │
│  Score: 78/100   │         │  Score: 72/100    │
│                  │         │                   │
│  Grammar:  85%   │         │  Grammar:  90%    │
│  Vocab:    72%   │         │  Vocab:    65%    │
│  Fillers:  4     │         │  Fillers:  7      │
│  Confidence: 80% │         │  Confidence: 70%  │
└──────────────────┘         └──────────────────┘

🏆 WINNER: You! (+150 bonus XP)
```

**Why this is a stretch-goal judge-killer:**

- Multiplayer AI is almost unheard of at hackathons
- "People can practice together and compete" makes this feel like a real product
- Even if not fully implemented, showing the CONCEPT in the UI is worth it
- Leaderboard creates viral loop (share your rank)

**Minimum Viable Version:** Don't need real multiplayer. Just let users see an anonymized leaderboard of scores. "You scored 78 on Job Interviews — that puts you in the top 15% of FluentAI users." Fake it with seeded data for the demo.

---

### Upgrade 8: Smarter Demo Video Strategy — The "Before/After" Moment (HIGH IMPACT, ZERO EFFORT)

**The Problem:**
The current demo video plan is a walkthrough of features. That's fine but forgettable.

**The Upgrade — Rewrite the demo video script:**

```
REVISED DEMO SCRIPT (2:00)

0:00-0:05  [Hook] "What if AI could make you sound like you went to Oxford?"

0:05-0:15  [Problem] Quick montage: someone fumbling a job interview,
           saying "um" 15 times, using basic vocabulary.
           Text overlay: "1.5 billion English learners. Zero AI speaking coaches."

0:15-0:25  [Split Screen — THE MOMENT]
           LEFT: Day 1 diagnostic — user stumbling, "basically um so like"
           RIGHT: Day 5 — same user, same topic, now articulate and confident
           Speech DNA radar chart morphing from small to large
           Text: "5 lessons. Same person."

0:25-0:40  [Product Tour] Speed-run: topic select → roadmap → prep material

0:40-1:10  [LIVE DEMO — The Money Shot]
           User starts a lesson. AI asks a question. User speaks.
           Camera zooms into the LIVE ANALYSIS SIDEBAR — mistakes appearing
           in real-time, vocabulary suggestions, filler word counter ticking.
           Ghost Whisper Coach gives a tip. User adjusts and nails the next answer.

1:10-1:30  [Report Card Reveal]
           Dramatic score animation. XP earned. Achievement unlocked.
           Then: "Hear Your Future Self" — user's OWN CLONED VOICE
           speaks the perfect version. (This is the gasp moment.)

1:30-1:45  [Technical Flex]
           Quick architecture diagram showing multi-agent system.
           "6 AI agents collaborating in real-time: Conversation, Analyzer,
           Coach, DNA, Gamification, Report."
           Flash: "ElevenLabs Conversational AI + Voice Cloning + Gemini Multimodal"

1:45-2:00  [Close]
           Speech DNA radar chart fully expanded.
           "FluentAI. Stop typing English. Start speaking it."
           Logo + GitHub link.
```

**Key change:** The "Before/After" split screen at 0:15-0:25 and the "Future You" voice clone at 1:10-1:30 are EMOTIONAL moments that judges remember. The current plan is feature-focused. This version is story-focused.

---

## Revised Technical Architecture (With Multi-Agent)

```
┌──────────────────────────────────────────────────────────────────┐
│                         FRONTEND (Next.js)                        │
│                                                                   │
│  ┌────────────┐ ┌──────────────┐ ┌─────────────┐ ┌───────────┐  │
│  │ Onboarding │ │ Lesson View  │ │  Report Card│ │ Speech DNA│  │
│  │ + Roadmap  │ │ + Ghost Coach│ │  + FutureYou│ │ + Battles │  │
│  └────────────┘ └──────┬───────┘ └─────────────┘ └───────────┘  │
│                        │                                          │
│      ┌─────────────────┼──────────────────┐                      │
│      │  ElevenLabs SDK │  WebSocket stream │  Audio Features     │
│      │  (voice call)   │  (live analysis)  │  (Web Audio API)   │
│      └─────────────────┼──────────────────┘                      │
└────────────────────────┼──────────────────────────────────────────┘
                         │
┌────────────────────────┼──────────────────────────────────────────┐
│           AGENT ORCHESTRATOR (Python asyncio event bus)           │
│                        │                                          │
│  ┌─────────────────────┼─────────────────────────────────────┐   │
│  │                 EVENT BUS                                  │   │
│  │  transcript_chunk | analysis_result | difficulty_adj |     │   │
│  │  dna_update | xp_earned | achievement_unlocked |          │   │
│  │  lesson_end | ghost_tip | slide_analysis                  │   │
│  └─────────────────────┬─────────────────────────────────────┘   │
│                        │                                          │
│  ┌──────────┐ ┌────────┴───┐ ┌───────────┐ ┌─────────────────┐  │
│  │CONVERSA- │ │ ANALYZER   │ │ COACH     │ │ DNA AGENT       │  │
│  │TION AGENT│ │ AGENT      │ │ AGENT     │ │ (Gemini)        │  │
│  │(11Labs)  │ │ (Gemini)   │ │ (Gemini)  │ │                 │  │
│  │          │ │            │ │           │ │ Updates profile  │  │
│  │ Voice    │ │ Grammar,   │ │ Adapts    │ │ in real-time.   │  │
│  │ call +   │ │ vocab,     │ │ difficulty│ │ Detects trends  │  │
│  │ personas │ │ fillers,   │ │ + ghost   │ │ mid-session.    │  │
│  │          │ │ idioms,    │ │ whisper   │ │                 │  │
│  │          │ │ audio feat │ │ tips      │ │                 │  │
│  └──────────┘ └────────────┘ └───────────┘ └─────────────────┘  │
│                                                                   │
│  ┌───────────────┐ ┌───────────────┐ ┌────────────────────────┐  │
│  │ GAMIFICATION  │ │ REPORT AGENT  │ │ PRESENTATION AGENT     │  │
│  │ AGENT         │ │ (Gemini)      │ │ (Gemini Multimodal)    │  │
│  │               │ │               │ │                        │  │
│  │ XP, levels,   │ │ End-of-call   │ │ Slide-aware analysis.  │  │
│  │ achievements, │ │ report card + │ │ Tracks coverage per    │  │
│  │ streaks,      │ │ ghost correct │ │ slide. Times pacing.   │  │
│  │ leaderboard   │ │ + "Future You"│ │ Only active in         │  │
│  │               │ │ voice clone   │ │ Presentation Mode.     │  │
│  └───────────────┘ └───────────────┘ └────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Revised Priority Stack (With New Upgrades)

**Must Have (Core — without this, the project doesn't work):**

1. Voice call with ElevenLabs agent
2. Live analysis sidebar during call (grammar + fillers + vocab)
3. Post-call report card with scores
4. Basic gamification (XP + level display)
5. **Multi-agent architecture** (event bus + at least 3 agents) ← NEW

**Should Have (Makes it impressive — aim for these):** 6. Speech DNA radar chart 7. Roadmap view (even if hardcoded) 8. Multiple personas 9. **"Future You" voice clone in report card** ← NEW (low effort, huge payoff) 10. **Adversarial "Pressure Mode" prompt** ← NEW (just a system prompt change)

**Nice To Have (Makes it mindblowing — stretch goals):** 11. Dynamic roadmap generation (Gemini) 12. **Ghost Whisper Coach mode** ← NEW 13. **Audio-level analysis (Web Audio API features)** ← NEW 14. Annotated replay mode 15. Achievement system with animations 16. Boss Battles 17. **Gemini Multimodal Presentation Mode** ← NEW

**Moonshot (Only if crushing it on time):** 18. **Speech Battles / Leaderboard** ← NEW 19. **Before/After split screen in demo video** ← NEW (zero code, just demo planning)

---

## Revised Hour-by-Hour Build Plan (~20 hours)

> Changes from original plan marked with ⚡

### Phase 1: Foundation (Hours 0-3) — SAME but add agent skeleton

**Hour 0-1: Project Bootstrap**

- Same as before: Next.js + FastAPI + SQLite + env vars + API key verification
- ⚡ **NEW:** Scaffold the `AgentOrchestrator` class + `BaseAgent` + event bus (30 min)
  - Just the skeleton — agents get filled in as we build features

**Hours 1-3: ElevenLabs Agent Setup**

- Same as before: Create agent, configure persona, knowledge base, tool calling
- ⚡ **NEW:** During diagnostic call, capture 30s audio clip for voice cloning (add to audio pipeline)
- ⚡ **NEW:** Create cloned voice via ElevenLabs API after diagnostic (background task)

### Phase 2: Core Loop (Hours 3-10) — Multi-Agent Integration

**Hours 3-5: Analysis Engine → ⚡ Now "Analyzer Agent"**

- Same Gemini analysis logic, but wrapped in `AnalyzerAgent` class
- Agent subscribes to `transcript_chunk` events, publishes `analysis_result`
- ⚡ **NEW:** `CoachAgent` subscribes to `analysis_result`, publishes `difficulty_adj`
- ⚡ **NEW:** `DNAAgent` subscribes to `analysis_result`, updates Speech DNA in real-time
- Frontend WebSocket now receives events from the orchestrator, not raw API calls

**Hours 5-7: Lesson View — SAME but with orchestrator**

- Same UI build, but backend uses event bus for all data flow
- ⚡ **NEW:** Add "Pressure Mode" toggle in lesson settings (different system prompt)

**Hours 7-9: Report Card — ⚡ Now with "Future You"**

- Same report generation via `ReportAgent`
- ⚡ **NEW:** After report generates, call ElevenLabs TTS with cloned voice + ghost correction text
- ⚡ **NEW:** Add "Hear Your Future Self" audio player to bottom of report card
- This is the demo's emotional climax — spend time making it look great

**Hours 9-10: Speech DNA — SAME**

### Phase 3: Progression System (Hours 10-14) — SAME

### Phase 4: Polish & Demo (Hours 14-20) — ⚡ Revised Demo Strategy

**Hours 14-16: UI/UX Polish — SAME**

**Hours 16-17: Stretch Features (Pick ONE):**

- Option A: Ghost Whisper Coach (if audio pipeline is solid)
- Option B: Presentation Mode with slides (if want to show Gemini multimodal)
- Option C: Annotated Replay Mode (original plan)

**Hours 17-18: End-to-End Testing — SAME**

**Hours 18-19: ⚡ REVISED Demo Video**

- Use the new demo script (Before/After + Future You + Architecture flex)
- Record a compelling diagnostic → lesson → report card flow
- Make sure "Future You" voice clone moment is captured
- Include 3-second architecture diagram flash showing multi-agent system

**Hours 19-20: Submission — SAME**

---

## Sentences That Win Hackathons

Drop these in the demo video, README, or when talking to judges:

- "We built a multi-agent system where 6 specialized AI agents collaborate in real-time during every voice call."
- "Our AI doesn't just read your words — it hears your confidence, your hesitation, your rhythm."
- "At the end of every lesson, you hear your own voice — cloned by AI — speaking the perfect version of what you tried to say."
- "A human tutor catches maybe 30% of your mistakes. Our system catches 100%, simultaneously, across 10 dimensions."
- "This isn't a chatbot. This is a speaking gym with an AI coach that knows every muscle you need to train."

---

_Build this. Win this. Shock them._
