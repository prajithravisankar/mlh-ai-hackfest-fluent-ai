# FluentAI — Build Todo

> Every checkbox below maps directly to planning.md. Complete them all top-to-bottom → ship a winning hackathon project.

---

## P00 — Pre-Hackathon Setup & Accounts

**Goal:** All accounts, API keys, content files, and local tooling ready BEFORE the clock starts.

- [ ] Accounts & API Keys
  - [ ] Create / verify ElevenLabs account with Conversational AI access
  - [ ] Generate ElevenLabs API key and store in password manager
  - [ ] Create / verify Google AI Studio account with Gemini 2.5 Flash access
  - [ ] Generate Gemini API key and store in password manager
  - [ ] Verify ElevenLabs API key with a hello-world TTS call
  - [ ] Verify Gemini API key with a hello-world prompt call
- [ ] ElevenLabs Platform Pre-Config
  - [ ] Create Conversational AI agent on the ElevenLabs dashboard ("FluentAI Coach")
  - [ ] Configure first persona: Coach Alex (warm, diagnostic voice — "Kore" or similar)
  - [ ] Test a basic voice conversation through the ElevenLabs playground to confirm it works
- [ ] Knowledge Base Content Files (write locally, upload in P01)
  - [ ] Write `grammar_rules.md` — Top 50 English grammar rules with examples
  - [ ] Write `idioms_database.md` — 200 common English idioms organized by topic
  - [ ] Write `evaluation_rubrics.md` — Scoring criteria for each Speech DNA dimension
  - [ ] Write `coaching_strategies.md` — How to adapt difficulty, encourage, push
- [ ] Local Tooling
  - [ ] Node.js 18+ installed and working
  - [ ] Python 3.11+ installed and working
  - [ ] Confirm `npx create-next-app` works
  - [ ] Confirm `pip install fastapi uvicorn` works
- [ ] Demo Prep
  - [ ] Write 3 demo talking-point scenarios (Job Interview, Casual Conversation, Presentation)
  - [ ] Practice speaking responses with intentional grammar mistakes, filler words, and vocabulary gaps (for demo recording later)

**Done when:** Both API keys return valid responses, ElevenLabs agent exists in dashboard, all 4 knowledge base files written, local tooling verified.

---

## P01 — Project Bootstrap & Scaffolding (Hour 0–1)

**Goal:** Both frontend and backend repos running locally, database schema created, project structure matches planning.md, multi-agent skeleton scaffolded.

- [ ] Frontend — Next.js
  - [ ] Run `npx create-next-app@latest frontend --typescript --tailwind --app --src-dir=false`
  - [ ] Verify `cd frontend && npm run dev` starts on localhost:3000
  - [ ] Install frontend dependencies: `npm install @11labs/react recharts framer-motion`
  - [ ] Create page route stubs (empty pages, just a title):
    - [ ] `app/page.tsx` — Landing / topic selection
    - [ ] `app/diagnostic/page.tsx` — Diagnostic call
    - [ ] `app/roadmap/page.tsx` — Roadmap view
    - [ ] `app/lesson/[id]/page.tsx` — Live lesson
    - [ ] `app/report/[id]/page.tsx` — Report card
    - [ ] `app/profile/page.tsx` — Speech DNA + achievements
    - [ ] `app/prep/[id]/page.tsx` — Pre-lesson study material
    - [ ] `app/replay/[id]/page.tsx` — Annotated call replay (stretch)
  - [ ] Create component file stubs (empty exports):
    - [ ] `components/VoiceCall.tsx`
    - [ ] `components/LiveAnalysisSidebar.tsx`
    - [ ] `components/TranscriptView.tsx`
    - [ ] `components/ReportCard.tsx`
    - [ ] `components/SpeechDNARadar.tsx`
    - [ ] `components/RoadmapView.tsx`
    - [ ] `components/AchievementPopup.tsx`
    - [ ] `components/LevelUpAnimation.tsx`
    - [ ] `components/PrepMaterial.tsx`
    - [ ] `components/GhostCorrection.tsx`
    - [ ] `components/WaveformVisualizer.tsx`
    - [ ] `components/ProgressBar.tsx`
  - [ ] Create lib file stubs:
    - [ ] `lib/api.ts` — Backend API client (empty functions)
    - [ ] `lib/websocket.ts` — WebSocket helpers
    - [ ] `lib/elevenlabs.ts` — ElevenLabs config
    - [ ] `lib/types.ts` — TypeScript type definitions
  - [ ] Set up dark theme base in `globals.css`
  - [ ] Create `app/layout.tsx` — root layout with site-wide nav bar (logo, nav links to roadmap/profile, XP bar placeholder)
- [ ] Backend — Python FastAPI
  - [ ] Create `backend/` directory
  - [ ] Create `backend/requirements.txt` with: `fastapi`, `uvicorn[standard]`, `websockets`, `aiosqlite`, `google-genai`, `elevenlabs`, `python-dotenv`, `pydantic`
  - [ ] Run `pip install -r backend/requirements.txt` (or use venv)
  - [ ] Create `backend/main.py` — FastAPI app with CORS middleware + health check `GET /api/health`
  - [ ] Verify `uvicorn main:app --reload` starts on localhost:8000
  - [ ] Create router stubs:
    - [ ] `backend/routers/__init__.py`
    - [ ] `backend/routers/lessons.py` — Lesson CRUD routes
    - [ ] `backend/routers/analysis.py` — ElevenLabs tool call endpoint
    - [ ] `backend/routers/roadmap.py` — Roadmap routes
    - [ ] `backend/routers/profile.py` — Speech DNA + XP routes
  - [ ] Create service stubs:
    - [ ] `backend/services/__init__.py`
    - [ ] `backend/services/gemini_analyzer.py`
    - [ ] `backend/services/roadmap_generator.py`
    - [ ] `backend/services/report_generator.py`
    - [ ] `backend/services/speech_dna.py`
    - [ ] `backend/services/gamification.py`
    - [ ] `backend/services/prep_generator.py`
  - [ ] Create model stubs:
    - [ ] `backend/models/__init__.py`
    - [ ] `backend/models/user.py`
    - [ ] `backend/models/lesson.py`
    - [ ] `backend/models/speech_dna.py`
    - [ ] `backend/models/roadmap.py`
  - [ ] Create ElevenLabs config:
    - [ ] `backend/elevenlabs_config/personas.py` — Character definitions
    - [ ] `backend/elevenlabs_config/knowledge_base/` — directory for content files
  - [ ] Copy knowledge base files into `backend/elevenlabs_config/knowledge_base/`
- [ ] Multi-Agent Skeleton
  - [ ] Create `backend/agents/__init__.py`
  - [ ] Create `backend/agents/orchestrator.py` — `AgentOrchestrator` class with in-memory event bus
  - [ ] Create `backend/agents/base_agent.py` — `BaseAgent` abstract class (subscribe, handle, publish)
  - [ ] Create agent stub files (empty classes extending BaseAgent):
    - [ ] `backend/agents/analyzer_agent.py` — subscribes to `transcript_chunk`
    - [ ] `backend/agents/coach_agent.py` — subscribes to `analysis_result`
    - [ ] `backend/agents/dna_agent.py` — subscribes to `analysis_result`
    - [ ] `backend/agents/gamification_agent.py` — subscribes to `analysis_result`, `lesson_end`
    - [ ] `backend/agents/report_agent.py` — subscribes to `lesson_end`
  - [ ] Wire orchestrator into `main.py` — register all agents on app startup
- [ ] Database
  - [ ] Create `backend/database.py` — async SQLite setup with `aiosqlite`
  - [ ] Define tables: `users`, `lessons`, `speech_dna_snapshots`, `roadmaps`, `achievements`, `lesson_analyses`
  - [ ] Auto-create tables on first startup
- [ ] Environment & Config
  - [ ] Create `backend/.env` with `ELEVENLABS_API_KEY`, `GEMINI_API_KEY`
  - [ ] Create `backend/.env.example` with placeholder values
  - [ ] Create `frontend/.env.local` with `NEXT_PUBLIC_BACKEND_URL=http://localhost:8000`, `NEXT_PUBLIC_ELEVENLABS_AGENT_ID`
  - [ ] Create `frontend/.env.example` with placeholder values
  - [ ] Configure `next.config.js` — API proxy rewrites from `/api` to backend during development
  - [ ] Create `.gitignore` at project root (node_modules, **pycache**, .env, .env.local, venv, .next, _.pyc, .DS_Store, _.db)
- [ ] Verify Everything Runs
  - [ ] Frontend starts without errors on localhost:3000
  - [ ] Backend starts without errors on localhost:8000
  - [ ] `GET /api/health` returns `{"status": "ok"}`
  - [ ] Git commit: "Initial project scaffold with multi-agent skeleton"

**Done when:** Both servers start, health check returns OK, all file stubs exist matching the project structure in planning.md, agent orchestrator skeleton is wired up.

---

## P02 — ElevenLabs Agent Setup & Voice Pipeline (Hours 1–3)

**Goal:** A working voice call between the frontend and ElevenLabs Conversational AI, with tool calls arriving at our backend.

- [ ] ElevenLabs Agent Configuration
  - [ ] Upload knowledge base files to ElevenLabs agent (grammar_rules, idioms_database, coaching_strategies, evaluation_rubrics)
  - [ ] Write system prompt for Coach Alex (diagnostic persona): warm, encouraging, asks open-ended questions, never scores during diagnostic
  - [ ] Configure tool calling on the ElevenLabs agent:
    - [ ] Define tool: `analyze_speech(transcript: str)` → returns analysis JSON
    - [ ] Define tool: `get_lesson_context()` → returns lesson objectives
    - [ ] Define tool: `end_lesson(final_transcript: str)` → triggers report generation
  - [ ] Set agent settings: server-managed turn detection, 10-min max duration, 10s silence prompt
  - [ ] Select voice for Coach Alex ("Kore" / warm male or similar)
  - [ ] Test agent in ElevenLabs playground — have a 2-min conversation and verify tool calls fire
- [ ] Backend Tool Call Endpoint
  - [ ] Implement `POST /api/tools/analyze_speech` in `backend/routers/analysis.py`
    - [ ] Accepts transcript chunk from ElevenLabs tool call
    - [ ] For now: returns a mock analysis JSON (real Gemini analysis comes in P03)
    - [ ] Publishes `transcript_chunk` event to the orchestrator
  - [ ] Implement `POST /api/tools/get_lesson_context` — returns current lesson objectives (mock data for now)
  - [ ] Implement `POST /api/tools/end_lesson` — triggers lesson end flow
  - [ ] Test: ElevenLabs agent calls our endpoint and receives a response
- [ ] Frontend Voice Call Integration
  - [ ] Implement `components/VoiceCall.tsx` using `@11labs/react` SDK
    - [ ] Connect to ElevenLabs Conversational AI agent
    - [ ] Handle microphone permissions
    - [ ] Show call status (connecting, active, ended)
    - [ ] Display basic waveform visualization during call
  - [ ] Create a test page: click "Start Call" → talk to Coach Alex → click "End Call"
  - [ ] Verify: user speaks → AI responds naturally → tool calls hit our backend
- [ ] Voice Cloning Pipeline (for "Future You" feature)
  - [ ] During the voice call, capture raw audio from the user's microphone using Web Audio API
  - [ ] After diagnostic call ends, send the best 30s audio clip to backend
  - [ ] Backend: `POST /api/voice/clone` — calls ElevenLabs Instant Voice Clone API to create a voice profile
  - [ ] Store the cloned voice ID in the user's profile in the database
  - [ ] Test: complete a diagnostic call → cloned voice ID exists in database
- [ ] WebSocket Setup
  - [ ] Implement WebSocket endpoint `ws://localhost:8000/ws/lesson/{lesson_id}` in `main.py`
  - [ ] Orchestrator publishes events → WebSocket broadcasts to connected frontend clients
  - [ ] Frontend: `lib/websocket.ts` — connect to WebSocket, parse incoming events
  - [ ] Test: trigger a mock event in backend → frontend receives it via WebSocket

**Done when:** User can have a full voice conversation with Coach Alex from the frontend, tool calls arrive at backend, WebSocket streams events to frontend, voice clone pipeline captures audio and creates a cloned voice.

---

## P03 — Gemini Analysis Engine + Analyzer Agent (Hours 3–5)

**Goal:** Real-time speech analysis via Gemini, delivered through the multi-agent architecture, streamed live to the frontend sidebar.

- [ ] Gemini Analysis Service
  - [ ] Implement `backend/services/gemini_analyzer.py`:
    - [ ] Initialize Gemini 2.5 Flash client
    - [ ] Write the `ANALYSIS_PROMPT` (from planning.md) — analyzes grammar, vocabulary, fillers, idioms, sentence complexity, confidence, pace, coherence
    - [ ] Function `analyze_transcript_chunk(transcript, speech_dna, lesson_objective)` → returns structured JSON
    - [ ] Add JSON schema validation — if Gemini returns malformed JSON, use fallback defaults
    - [ ] Test: send 3 sample transcript chunks → verify valid JSON analysis for each
  - [ ] Tune the analysis prompt
    - [ ] Test with good English sample → expect high scores
    - [ ] Test with bad English sample (filler words, grammar errors) → expect low scores + specific error list
    - [ ] Test with intermediate sample → expect nuanced feedback with missed opportunities
    - [ ] Adjust prompt until scoring feels accurate and consistent
- [ ] Analyzer Agent (Multi-Agent)
  - [ ] Implement `backend/agents/analyzer_agent.py`:
    - [ ] Subscribes to `transcript_chunk` events
    - [ ] Calls `gemini_analyzer.analyze_transcript_chunk()`
    - [ ] Publishes `analysis_result` event with structured analysis data
    - [ ] Maintains a running buffer of all analysis chunks for the current session
  - [ ] Test: publish a `transcript_chunk` event → receive `analysis_result` event
- [ ] Coach Agent (Multi-Agent)
  - [ ] Implement `backend/agents/coach_agent.py`:
    - [ ] Subscribes to `analysis_result` events
    - [ ] Logic: if grammar score < 50 → publish `difficulty_adj` event (easier)
    - [ ] Logic: if grammar score > 85 AND vocabulary > 80 → publish `difficulty_adj` (harder)
    - [ ] Tracks patterns across multiple chunks (e.g., "user keeps making same grammar error")
  - [ ] The `difficulty_adj` event is returned to ElevenLabs via the next tool call response, so the AI character adapts
- [ ] DNA Agent (Multi-Agent)
  - [ ] Implement `backend/agents/dna_agent.py`:
    - [ ] Subscribes to `analysis_result` events
    - [ ] Updates the user's Speech DNA profile in real-time as analysis comes in
    - [ ] Publishes `dna_update` event with current DNA snapshot
  - [ ] Test: multiple analysis events → DNA profile reflects running averages
- [ ] Wire Tool Call → Orchestrator → WebSocket
  - [ ] Update `POST /api/tools/analyze_speech` to:
    - [ ] Publish `transcript_chunk` event to orchestrator (instead of direct analysis)
    - [ ] Wait for `analysis_result` event from the Analyzer Agent
    - [ ] Return analysis to ElevenLabs (so AI character can adapt)
    - [ ] Push `analysis_result` to frontend via WebSocket simultaneously
  - [ ] Test full loop: speak during call → ElevenLabs sends tool call → backend publishes event → agents process → WebSocket sends analysis to frontend
- [ ] Frontend: Live Analysis Sidebar
  - [ ] Implement `components/LiveAnalysisSidebar.tsx`:
    - [ ] Connect to WebSocket for `analysis_result` events
    - [ ] Display live updating stats: Grammar %, Vocabulary %, Filler count, Pace WPM, Complexity, Coherence, Confidence
    - [ ] Color coding: green (>75%), yellow (50-75%), red (<50%)
    - [ ] Show live mistakes list: timestamp + what they said + correction
    - [ ] Show missed opportunities: better word choices, idioms they could have used
  - [ ] Smooth animations on stat updates (numbers counting up/down)
  - [ ] Test: during a live call, sidebar updates every ~15 seconds with real analysis

**Done when:** During a voice call, the sidebar shows live grammar/vocab/filler scores updating in real-time, with specific mistakes and suggestions appearing as the user speaks. All analysis flows through the multi-agent event bus.

---

## P04 — Lesson View — The Core Screen (Hours 5–7)

**Goal:** The full lesson experience — voice call + live analysis + transcript + timer — all working together on one screen.

- [ ] Lesson Session Management (Backend)
  - [ ] Implement `POST /api/lessons/start` — creates a lesson session, returns lesson_id
    - [ ] Accepts: user_id, lesson config (title, objectives, character, target vocabulary/idioms)
    - [ ] Creates lesson record in database with status "active"
    - [ ] Initializes the orchestrator session for this lesson
    - [ ] Returns: lesson_id, ElevenLabs agent config (system prompt customized for this lesson)
  - [ ] Implement `POST /api/lessons/{id}/end` — ends the lesson session
    - [ ] Publishes `lesson_end` event to orchestrator
    - [ ] Updates lesson status to "completed" in database
    - [ ] Returns: lesson_id for report card redirect
  - [ ] Implement `GET /api/lessons/{id}` — returns lesson data + analysis history
- [ ] Dynamic ElevenLabs Agent Prompts
  - [ ] Create `backend/elevenlabs_config/personas.py` with character definitions:
    - [ ] Coach Alex: warm, diagnostic, open-ended (for diagnostic calls)
    - [ ] Sarah Chen (HR): professional, structured, behavioral questions (for interview lessons)
    - [ ] David Park (VP): authoritative, challenging, high expectations (for advanced/boss battles)
  - [ ] System prompt template that injects: character persona + lesson objectives + target vocabulary + user's weak areas from Speech DNA
  - [ ] "Pressure Mode" system prompt variant: adversarial, interrupts, challenges, rapid-fire
- [ ] Frontend: Full Lesson Page (`app/lesson/[id]/page.tsx`)
  - [ ] Layout: two-column — left (voice call + transcript), right (live analysis sidebar)
  - [ ] Top bar: lesson title, character info (name + role + avatar), timer, "Pressure Mode" toggle
  - [ ] Integrate `VoiceCall.tsx` component (left column)
  - [ ] Integrate `LiveAnalysisSidebar.tsx` component (right column)
  - [ ] Implement `components/TranscriptView.tsx`:
    - [ ] Scrolling transcript that updates as user/AI speaks
    - [ ] Highlight grammar errors inline (red underline)
    - [ ] Highlight filler words inline (yellow)
    - [ ] Show "better word" suggestions as inline tooltips
  - [ ] Implement `components/WaveformVisualizer.tsx`:
    - [ ] Web Audio API — visualize audio waveform during call
    - [ ] Show for both user's mic and AI's voice
  - [ ] Call controls: "End Call" button, "Pause" button, lesson timer
  - [ ] Lesson start flow: page loads → fetch lesson config from backend → start ElevenLabs call with custom system prompt → WebSocket connects
  - [ ] Lesson end flow: click "End Call" → call `POST /api/lessons/{id}/end` → redirect to report card page
- [ ] End-to-End Lesson Test
  - [ ] Start a lesson → have a 3-min voice conversation → see live analysis in sidebar → see transcript with highlights → end call → lesson record saved in database
  - [ ] Test "Pressure Mode" toggle: switch on → AI character becomes adversarial

**Done when:** The full lesson screen works — user has a voice conversation, sees live stats, scrolling transcript with error highlights, and can end the call. Pressure Mode toggle changes AI behavior.

---

## P05 — Report Card Generation (Hours 7–9)

**Goal:** After every lesson, generate a beautiful, detailed report card with scores, key moments, ghost corrections, and the "Future You" voice clone reveal.

- [ ] Report Generation Service (Backend)
  - [ ] Implement `backend/services/report_generator.py`:
    - [ ] Function `generate_report(lesson_id)`:
      - [ ] Fetch all analysis chunks for this lesson from database
      - [ ] Aggregate scores: weighted average across all chunks per dimension
      - [ ] Identify "Key Moments": best moment (highest scores), worst moment (lowest scores), biggest missed opportunity
    - [ ] Gemini prompt for natural language insights:
      - [ ] "Here are the aggregated scores and key moments. Write a 3-sentence coaching insight."
    - [ ] Gemini prompt for ghost corrections:
      - [ ] "Here is the user's worst transcript segment. Rewrite it as an expert English speaker would say it, keeping the same ideas."
    - [ ] Return full report JSON: overall score, dimension breakdown, key moments, ghost correction text, AI insight
  - [ ] Test: generate report from mock lesson data → verify all fields populated
- [ ] Report Agent (Multi-Agent)
  - [ ] Implement `backend/agents/report_agent.py`:
    - [ ] Subscribes to `lesson_end` event
    - [ ] Calls `report_generator.generate_report()`
    - [ ] Publishes `report_ready` event with full report data
  - [ ] Test: publish `lesson_end` → receive `report_ready` with valid report
- [ ] "Future You" Voice Clone Generation
  - [ ] After report generates, take the ghost correction text
  - [ ] Call ElevenLabs TTS API with the user's cloned voice ID + ghost correction text
  - [ ] Store the generated audio URL/blob
  - [ ] Include `future_you_audio_url` in the report response
  - [ ] Fallback: if voice cloning failed/unavailable, use a default ElevenLabs voice instead
- [ ] Report Card API Endpoint
  - [ ] Implement `GET /api/reports/{lesson_id}` — returns full report JSON + future_you audio
  - [ ] Implement `POST /api/reports/{lesson_id}/generate` — triggers report generation if not yet done
- [ ] Frontend: Report Card Page (`app/report/[id]/page.tsx`)
  - [ ] Implement `components/ReportCard.tsx`:
    - [ ] Overall score with animated counter (0 → 72, counting up) using Framer Motion
    - [ ] XP earned badge + streak display
    - [ ] Dimension breakdown: horizontal progress bars for each dimension (Grammar, Vocabulary, Filler Words, Complexity, Idioms, Pace, Coherence, Confidence)
    - [ ] Color coding per bar: green/yellow/red + delta from last lesson (+5%, -2%, etc.)
    - [ ] "Key Moments" section:
      - [ ] ✅ Great moment (green card) — quote + why it was good
      - [ ] ❌ Fix moment (red card) — what they said → what they should say + grammar rule
      - [ ] 💡 Missed opportunity (blue card) — context + suggested idiom/vocabulary
  - [ ] Implement `components/GhostCorrection.tsx`:
    - [ ] Side-by-side: "What you said" (left, red tint) vs "Expert version" (right, green tint)
    - [ ] Highlight specific improvements (stronger verb, removed fillers, added idiom)
  - [ ] "Future You" Audio Player:
    - [ ] Audio player at bottom of report card with waveform visualization
    - [ ] Label: "🔮 Hear Your Future Self"
    - [ ] Show the ghost correction text alongside the audio
    - [ ] Play/pause button with progress bar
    - [ ] This is the emotional climax — make it visually prominent
  - [ ] Navigation: "Next Lesson" button, "Replay Call" button, "Share" button
  - [ ] Score reveal animation: page loads → brief suspense → score animates in → dimension bars fill → key moments fade in → "Future You" section reveals last
- [ ] End-to-End Report Test
  - [ ] Complete a lesson → navigate to report card → see animated score reveal → see dimension breakdown → read key moments → play "Future You" audio
  - [ ] Test with different quality levels: poor speaker → expect low scores + many fixes. Good speaker → expect high scores + few fixes

**Done when:** After every lesson, a beautiful animated report card appears with scores, key moments, ghost corrections, and the "Future You" cloned voice audio playing the corrected version.

---

## P06 — Speech DNA System (Hours 9–10)

**Goal:** Build the persistent Speech DNA profile — a radar chart showing the user's multi-dimensional speaking fingerprint that evolves over time.

- [ ] Speech DNA Service (Backend)
  - [ ] Implement `backend/services/speech_dna.py`:
    - [ ] Function `compute_dna(user_id)`: aggregate all historical lesson scores into a single DNA profile
    - [ ] DNA dimensions: grammar, vocabulary, filler_words, sentence_complexity, idiom_usage, speaking_pace, coherence, confidence
    - [ ] Each dimension: current score (0-100), trend (improving/stagnant/declining), history (last 10 values)
    - [ ] Function `update_dna(user_id, lesson_analysis)`: incorporate latest lesson into DNA
    - [ ] Function `generate_dna_insight(dna)`: Gemini writes a natural language paragraph about trajectory and focus areas
  - [ ] Store DNA snapshots in database after each lesson
  - [ ] Test: create user → complete 2 lessons → DNA shows averaged scores + trends
- [ ] Speech DNA API
  - [ ] Implement `GET /api/profile/{user_id}/dna` — returns current DNA + trends + insight
  - [ ] Implement `GET /api/profile/{user_id}/dna/history` — returns DNA snapshots over time
- [ ] Frontend: Speech DNA Page (`app/profile/page.tsx`)
  - [ ] Implement `components/SpeechDNARadar.tsx`:
    - [ ] Recharts radar chart with 8 axes (one per dimension)
    - [ ] Current scores plotted as a filled polygon
    - [ ] Optional: overlay previous session's polygon (semi-transparent) to show growth
    - [ ] Animated: polygon morphs from old shape to new shape on load
  - [ ] Trends section below radar:
    - [ ] Per-dimension: score + arrow (📈📉➡️) + delta + short note
  - [ ] Tags section: auto-generated tags like `#GrammarImprover`, `#NeedsIdioms`, `#FillerWordSlayer`
  - [ ] AI Insight section: Gemini-generated paragraph about the user's speaking trajectory
  - [ ] Link from Report Card page: "📈 Your Speech DNA Updated" → navigate to profile
- [ ] Test: complete 2-3 lessons → profile page shows radar chart with real data + trends + AI insight

**Done when:** The radar chart shows real scores across 8 dimensions, trends show improvement/decline per dimension, and the AI writes a coaching insight paragraph. DNA updates after every lesson.

---

## P07 — Gamification Engine (Hours 10–11)

**Goal:** XP, levels, streaks, and achievements make every lesson feel rewarding and create a retention loop.

- [ ] Gamification Service (Backend)
  - [ ] Implement `backend/services/gamification.py`:
    - [ ] Function `calculate_xp(lesson_analysis)`:
      - [ ] Base XP: 100 per completed lesson
      - [ ] Grammar bonus: +5 XP per clean sentence
      - [ ] Vocabulary bonus: +10 XP per advanced word used
      - [ ] Idiom bonus: +25 XP per idiom used correctly
      - [ ] Zero filler bonus: +50 XP for <3 filler words
      - [ ] Perfect score bonus: +200 XP for 90%+ overall
      - [ ] Streak multiplier: Day 3+ = 1.5x, Day 7+ = 2x
    - [ ] Function `check_level_up(user)`: determine if XP crosses level threshold
      - [ ] Level thresholds: 0, 500, 1500, 3500, 7000, 12000
      - [ ] Level names: "Getting Started", "Finding Your Voice", "Building Confidence", "Getting Sharp", "Commanding Presence", "Dangerously Articulate"
    - [ ] Function `check_achievements(user, lesson_analysis)`:
      - [ ] First Words, Grammar Guardian, Filler Slayer, Idiom Master, Speed Demon, Vocabulary Vault, Boss Slayer, Streak Machine
    - [ ] Function `update_streak(user)`: increment or reset daily streak
- [ ] Gamification Agent (Multi-Agent)
  - [ ] Implement `backend/agents/gamification_agent.py`:
    - [ ] Subscribes to `analysis_result` events (for real-time XP preview)
    - [ ] Subscribes to `lesson_end` events (for final XP calculation + achievement check)
    - [ ] Publishes `xp_earned` event with XP breakdown
    - [ ] Publishes `achievement_unlocked` event if any achievement triggered
    - [ ] Publishes `level_up` event if user crosses level threshold
  - [ ] Test: mock lesson end → correct XP calculated, achievements checked
- [ ] Gamification API
  - [ ] Implement `GET /api/profile/{user_id}/stats` — returns XP, level, streak, achievements
- [ ] Frontend: Gamification UI
  - [ ] `components/ProgressBar.tsx`:
    - [ ] XP bar showing current XP / next level threshold
    - [ ] Level name + number
    - [ ] Streak flame icon + day count
    - [ ] Show in header/nav on every page
  - [ ] `components/AchievementPopup.tsx`:
    - [ ] Animated popup when achievement unlocked (Framer Motion: slide in from right, gold glow)
    - [ ] Achievement icon + name + description
    - [ ] Auto-dismiss after 3 seconds
  - [ ] `components/LevelUpAnimation.tsx`:
    - [ ] Full-screen overlay animation when user levels up
    - [ ] Show new level name + congratulations
    - [ ] Confetti or particle effect
  - [ ] Show XP breakdown in report card: base + grammar bonus + vocab bonus etc.
  - [ ] Show earned achievements in report card "Power-ups Unlocked" section
- [ ] Test: complete lessons → XP counts up, level bar fills, achievements pop up, level-up animation triggers on threshold

**Done when:** After every lesson, XP is calculated and displayed with a breakdown, achievements trigger with animated popups, and leveling up shows a celebration animation.

---

## P08 — Roadmap System (Hours 11–13)

**Goal:** Personalized curriculum generated by Gemini — visual lesson tree with levels, lessons, and boss battles that reshuffles based on Speech DNA.

- [ ] Roadmap Generation Service (Backend)
  - [ ] Implement `backend/services/roadmap_generator.py`:
    - [ ] Function `generate_roadmap(goal, speech_dna)`:
      - [ ] Gemini prompt using `ROADMAP_PROMPT` from planning.md
      - [ ] Returns structured JSON: levels → lessons → boss battles
      - [ ] Each lesson: title, description, character, target dimensions, target vocab/idioms, duration, pass threshold
    - [ ] Function `reshuffle_roadmap(user_id)`:
      - [ ] After each lesson, check Speech DNA for changes
      - [ ] If a dimension improved significantly → skip/demote related lessons
      - [ ] If a dimension declined or stagnated → inject focused lessons
      - [ ] Gemini decides the reshuffling based on DNA delta
    - [ ] Fallback: if Gemini generation fails or is slow, return a hardcoded "Job Interviews" roadmap
  - [ ] Store roadmap in database per user per goal
  - [ ] Test: provide Speech DNA + "Job Interviews" → get a valid roadmap with 3-4 levels
- [ ] Roadmap API
  - [ ] Implement `POST /api/roadmap/generate` — generates roadmap from goal + diagnostic DNA
  - [ ] Implement `GET /api/roadmap/{user_id}` — returns current roadmap with lesson statuses
  - [ ] Implement `POST /api/roadmap/{user_id}/reshuffle` — triggers DNA-based reshuffling
- [ ] Onboarding Flow (Backend + Frontend)
  - [ ] `app/page.tsx` — Landing page:
    - [ ] Compelling headline: "Stop typing English. Start speaking it."
    - [ ] Goal selection cards: Job Interviews, Public Speaking, Sales & Negotiation, Casual Conversation, Academic Presentations, Business English, Custom
    - [ ] Custom input field for free-text goals
    - [ ] "Start" button → creates user → navigates to diagnostic
  - [ ] `app/diagnostic/page.tsx` — Diagnostic call page:
    - [ ] Brief intro: "Let's chat for 5 minutes so I can understand your level"
    - [ ] Embedded VoiceCall component (Coach Alex persona)
    - [ ] After call ends → show "Generating your personalized roadmap..." loading
    - [ ] Call `POST /api/roadmap/generate` with diagnostic DNA + chosen goal
    - [ ] Navigate to roadmap page
- [ ] Frontend: Roadmap Page (`app/roadmap/page.tsx`)
  - [ ] Implement `components/RoadmapView.tsx`:
    - [ ] Visual tree/timeline: levels stacked vertically, lessons as nodes
    - [ ] Level sections: name, difficulty badge, progress bar (X/Y lessons complete)
    - [ ] Lesson nodes: title, character avatar, status (locked/available/completed/failed)
    - [ ] Boss Battle nodes: special styling (gold border, larger, 🏆 icon)
    - [ ] Completed lessons: checkmark + score displayed
    - [ ] Locked lessons: greyed out with lock icon
    - [ ] Current available lesson: highlighted, pulsing "Start" button
    - [ ] Click lesson → navigate to prep page (if available) or start lesson directly
  - [ ] "Roadmap Updated" notification after DNA changes cause reshuffling
- [ ] Test: select "Job Interviews" → complete diagnostic → roadmap appears with levels and lessons → complete a lesson → roadmap updates (lesson marked complete, next unlocked)

**Done when:** User selects a goal, does a diagnostic call, sees a personalized multi-level roadmap, and can navigate from roadmap → prep → lesson → report → updated roadmap.

---

## P09 — Preparation Mode (Hours 13–14)

**Goal:** Before each lesson, the user can study AI-generated prep material tailored to their weaknesses.

- [ ] Prep Generation Service (Backend)
  - [ ] Implement `backend/services/prep_generator.py`:
    - [ ] Function `generate_prep(lesson_config, speech_dna)`:
      - [ ] Gemini generates: lesson objective, key vocabulary to use, phrases to practice, relevant idioms, sample questions they'll face
      - [ ] Vocabulary and idioms are specifically chosen based on what the user is WEAK at (from Speech DNA)
      - [ ] Estimated call duration
    - [ ] Return structured JSON
  - [ ] Test: provide lesson config + DNA → get valid prep material
- [ ] Prep API
  - [ ] Implement `GET /api/prep/{lesson_id}` — returns prep material for a lesson
- [ ] Frontend: Prep Page (`app/prep/[id]/page.tsx`)
  - [ ] Implement `components/PrepMaterial.tsx`:
    - [ ] Lesson objective card (what you'll practice)
    - [ ] Vocabulary cards: word + definition + "instead of [basic word]"
    - [ ] Phrases to practice: displayed as quotable cards
    - [ ] Idioms section: idiom + meaning + usage example
    - [ ] Sample questions preview
    - [ ] "Start Lesson" button at bottom → navigates to lesson page
  - [ ] Clean, study-card style layout
- [ ] Wire prep into roadmap: clicking a lesson in roadmap → shows prep page → "Start Lesson" button → lesson page
- [ ] Test: click upcoming lesson in roadmap → see relevant prep material → start lesson

**Done when:** Users can view personalized study material before each lesson, with vocabulary and idioms targeted at their weak points.

---

## P10 — UI/UX Polish & Dark Theme (Hours 14–16)

**Goal:** The entire app looks polished, cohesive, and demo-ready with a dark theme, smooth animations, and proper states.

- [ ] Global Styling
  - [ ] Dark theme as default: dark backgrounds, light text, accent colors for scores
  - [ ] Color palette: dark navy/charcoal background, vibrant green (good), amber (okay), red (bad), blue (info), gold (achievements)
  - [ ] Typography: clean sans-serif, clear hierarchy (headings, body, stats)
  - [ ] Consistent spacing and card styles across all pages
- [ ] Landing Page Polish
  - [ ] Hero section: headline, subheadline, visual (screenshot or illustration)
  - [ ] Goal selection cards with icons and hover effects
  - [ ] Smooth page transition to diagnostic
- [ ] Lesson Page Polish
  - [ ] Clean two-column layout that doesn't feel cramped
  - [ ] Sidebar stats have smooth number transitions
  - [ ] Transcript scrolls smoothly with highlighted errors
  - [ ] Call controls are prominent and clear
- [ ] Report Card Polish
  - [ ] Staggered animation: score → bars → key moments → "Future You"
  - [ ] Score counter animation (0 → final score, counting up)
  - [ ] Dimension bars fill animation (left to right)
  - [ ] Key moment cards fade in sequentially
- [ ] Speech DNA Polish
  - [ ] Radar chart animation (polygon morphs from zero to current shape)
  - [ ] Trends section is scannable at a glance
- [ ] Roadmap Polish
  - [ ] Visual tree feels like a game progression screen
  - [ ] Completed nodes have satisfying checkmarks
  - [ ] Locked nodes are clearly greyed out
- [ ] Page Transitions
  - [ ] Framer Motion page transitions between all routes
  - [ ] Loading states for all async operations (generating roadmap, generating report, etc.)
  - [ ] Empty states for pages with no data yet
  - [ ] Error states with retry buttons
- [ ] Responsive
  - [ ] Works on laptop screens (primary demo target)
  - [ ] Doesn't break on smaller screens (nice to have)
- [ ] Architecture Diagram
  - [ ] Create multi-agent architecture diagram image (use draw.io, Excalidraw, or Mermaid → PNG)
  - [ ] Save as `demo/architecture.png` — needed for demo video tech flex section and README
- [ ] Architecture Diagram
  - [ ] Create multi-agent architecture diagram image (use draw.io, Excalidraw, or Mermaid → PNG)
  - [ ] Save as `demo/architecture.png` — needed for demo video tech flex section and README

**Done when:** Every page looks polished, animations are smooth, dark theme is consistent, and there are no visual glitches during the demo flow.

---

## P11 — Stretch Features — Pick Based on Time (Hours 16–17)

**Goal:** Add ONE high-impact stretch feature to differentiate further. Pick based on available time and what's most demo-worthy.

### Option A: Annotated Call Replay

- [ ] Backend: store full transcript with timestamps + per-segment analysis in database
- [ ] Backend: `GET /api/replay/{lesson_id}` — returns timestamped transcript + annotations
- [ ] Frontend: `app/replay/[id]/page.tsx`:
  - [ ] Scrolling transcript with inline error highlights, filler word marks, ghost corrections
  - [ ] "Jump to Mistakes Only" filter
  - [ ] Ghost correction displayed below each problematic segment
- [ ] Link from report card: "Replay Call With Annotations" button

### Option B: Ghost Whisper Coach Mode

- [ ] Backend: lightweight Gemini endpoint for real-time coaching tips (short, 1-sentence suggestions)
- [ ] Frontend: Web Audio API second audio channel for ghost coach
- [ ] ElevenLabs TTS for ghost voice (different voice, lower volume, faster speed)
- [ ] Ghost only speaks during pauses (silence > 1.5s detection)
- [ ] Toggle on/off in lesson view
- [ ] Test: during call, ghost whispers vocabulary/idiom suggestions

### Option C: Audio-Level Analysis

- [ ] Frontend: Web Audio API feature extraction (volume, pitch variation, pause patterns)
- [ ] Send audio features alongside transcript to backend every 5 seconds
- [ ] Backend: include audio features in analysis (new Speech DNA dimensions: Vocal Confidence, Expressiveness, Rhythm)
- [ ] Frontend: show audio-based metrics in sidebar (monotone warning, confidence meter)

### Option D: Gemini Multimodal Presentation Mode

- [ ] Frontend: slide upload (PDF/images) on lesson start for Presentation goals
- [ ] Backend: convert uploaded slides to images, store per lesson
- [ ] Backend: send current slide image + transcript to Gemini multimodal for slide-aware analysis
- [ ] Frontend: show slide preview in lesson view + slide coverage checklist + per-slide timing
- [ ] AI analyzes whether user covered key slide points, spent appropriate time, and matched visual data

**Done when:** One stretch feature is fully working and demo-ready.

---

## P12 — End-to-End Testing & Bug Fixes (Hours 17–18)

**Goal:** The complete demo flow works flawlessly from start to finish with zero crashes.

- [ ] Full Demo Flow Test
  - [ ] Fresh start: open landing page → select "Job Interviews"
  - [ ] Diagnostic: have a 3-5 min call with Coach Alex → call ends cleanly
  - [ ] Roadmap: personalized roadmap appears with levels and lessons
  - [ ] Prep: click first lesson → see prep material → click "Start Lesson"
  - [ ] Lesson: have a 3-5 min lesson → live analysis sidebar works → transcript highlights work
  - [ ] End call: click "End Call" → redirect to report card
  - [ ] Report: animated score reveal → dimension breakdown → key moments → "Future You" audio plays
  - [ ] Profile: navigate to Speech DNA → radar chart shows data → trends + insight present
  - [ ] Repeat: start another lesson → verify DNA updated → verify XP increased → verify roadmap progressed
- [ ] Edge Case Testing
  - [ ] What happens if user speaks only 2 sentences? (short call)
  - [ ] What happens if Gemini returns an error? (fallback handling)
  - [ ] What happens if ElevenLabs call drops? (error recovery)
  - [ ] What happens if WebSocket disconnects mid-lesson? (reconnection)
  - [ ] What happens if user has no previous lessons? (empty state handling)
- [ ] Bug Fix Pass
  - [ ] Fix any broken transitions between pages
  - [ ] Fix any visual glitches in animations
  - [ ] Fix any data inconsistencies (XP not matching, DNA not updating)
  - [ ] Fix any WebSocket connection issues
- [ ] Performance Check
  - [ ] Analysis results arrive within 2-3 seconds of speaking
  - [ ] Report generation completes within 5 seconds of call ending
  - [ ] No noticeable lag in UI updates
- [ ] Prepare Demo Scenario
  - [ ] Choose the best topic and lesson for the demo video
  - [ ] Practice the demo flow 2-3 times
  - [ ] Prepare intentional mistakes to speak during the demo (to showcase the analysis)

**Done when:** The full flow works 3 times in a row without errors. Demo scenario is rehearsed.
2.5 — Deployment (Hour 17.5–18)

**Goal:** App is live on the internet for the demo video and judges to access.

- [ ] Frontend Deployment (Vercel)
  - [ ] Push frontend to GitHub (if not already)
  - [ ] Connect repo to Vercel and import the `frontend/` directory
  - [ ] Set environment variables in Vercel dashboard: `NEXT_PUBLIC_BACKEND_URL`, `NEXT_PUBLIC_ELEVENLABS_AGENT_ID`
  - [ ] Deploy and verify landing page loads on the Vercel URL
  - [ ] Test full flow on deployed frontend
- [ ] Backend Deployment (Railway or Render)
  - [ ] Create a new project on Railway (or Render)
  - [ ] Connect the `backend/` directory
  - [ ] Set environment variables: `ELEVENLABS_API_KEY`, `GEMINI_API_KEY`, `CORS_ORIGINS` (Vercel URL)
  - [ ] Deploy and verify `GET /api/health` returns OK on the public URL
  - [ ] Update Vercel frontend env var `NEXT_PUBLIC_BACKEND_URL` to point to deployed backend
- [ ] End-to-End on Deployed App
  - [ ] Full demo flow works on live URLs (not localhost)
  - [ ] WebSocket connection works through deployed backend
  - [ ] No CORS errors in browser console

**Done when:** Both frontend and backend are live, connected, and the full demo flow works on public URLs.

---

## P1

---

## P12.5 — Deployment (Hour 17.5–18)

**Goal:** App is live on the internet for the demo video and judges to access.

- [ ] Frontend Deployment (Vercel)
  - [ ] Push frontend to GitHub (if not already)
  - [ ] Connect repo to Vercel and import the `frontend/` directory
  - [ ] Set environment variables in Vercel dashboard: `NEXT_PUBLIC_BACKEND_URL`, `NEXT_PUBLIC_ELEVENLABS_AGENT_ID`
  - [ ] Deploy and verify landing page loads on the Vercel URL
  - [ ] Test full flow on deployed frontend
- [ ] Backend Deployment (Railway or Render)
  - [ ] Create a new project on Railway (or Render)
  - [ ] Connect the `backend/` directory
  - [ ] Set environment variables: `ELEVENLABS_API_KEY`, `GEMINI_API_KEY`, `CORS_ORIGINS` (Vercel URL)
  - [ ] Deploy and verify `GET /api/health` returns OK on the public URL
  - [ ] Update Vercel frontend env var `NEXT_PUBLIC_BACKEND_URL` to point to deployed backend
- [ ] End-to-End on Deployed App
  - [ ] Full demo flow works on live URLs (not localhost)
  - [ ] WebSocket connection works through deployed backend
  - [ ] No CORS errors in browser console

**Done when:** Both frontend and backend are live, connected, and the full demo flow works on public URLs.

---

## P13 — Demo Video Recording (Hours 18–19)

**Goal:** Record a compelling 2-minute demo video following the revised demo script from planning.md.

- [ ] Setup
  - [ ] Screen recording software ready (OBS, QuickTime, or Loom)
  - [ ] Good microphone + quiet environment
  - [ ] App running locally with clean data (fresh user)
  - [ ] Architecture diagram image ready for the "tech flex" section
- [ ] Record — Following Revised Demo Script
  - [ ] 0:00–0:05 — Hook: "What if AI could make you sound like you went to Oxford?"
  - [ ] 0:05–0:15 — Problem: show text overlays about 1.5B English learners, no AI coaches
  - [ ] 0:15–0:25 — Before/After split: show diagnostic (stumbling) vs later lesson (articulate) with Speech DNA morphing
  - [ ] 0:25–0:40 — Product tour: topic selection → roadmap → prep material (speed-run)
  - [ ] 0:40–1:10 — LIVE DEMO: start a lesson, speak, show live analysis sidebar updating, mistakes appearing, filler counter ticking
  - [ ] 1:10–1:30 — Report card reveal: score animation, XP earned, then "Future You" voice clone playing
  - [ ] 1:30–1:45 — Tech flex: flash architecture diagram, mention "6 AI agents collaborating in real-time", "ElevenLabs + Gemini Multimodal"
  - [ ] 1:45–2:00 — Close: Speech DNA radar chart, "FluentAI. Stop typing English. Start speaking it.", logo + GitHub
- [ ] Post-Production (minimal)
  - [ ] Trim dead air and loading screens
  - [ ] Add text overlays for hook and close
  - [ ] Add background music (optional, low volume)
  - [ ] Ensure video is under 2:00
  - [ ] Export in 1080p

**Done when:** 2-minute video is recorded, edited, and exported. It follows the emotional arc: hook → problem → solution → live demo → payoff → tech flex → close.

---

## P14 — README, Submission & Ship (Hours 19–20)

**Goal:** Public GitHub repo is ready, Devpost submission is complete, everything is shipped.

- [ ] README.md
  - [ ] Project title + one-liner description
  - [ ] Problem statement (1.5B English learners, no AI speaking coaches)
  - [ ] Solution description (what FluentAI does)
  - [ ] Key features list (voice calls, live analysis, report cards, Speech DNA, gamification, multi-agent architecture, voice cloning)
  - [ ] Screenshots / GIFs of: landing page, lesson view, report card, Speech DNA
  - [ ] Architecture diagram (the multi-agent one)
  - [ ] Tech stack table
  - [ ] How to run locally (frontend + backend setup instructions)
  - [ ] API integrations explained (ElevenLabs, Gemini)
  - [ ] Team members
- [ ] GitHub Repo
  - [ ] Verify `.gitignore` excludes: node_modules, .env, **pycache**, venv, .next, \*.db
  - [ ] Verify no API keys are committed
  - [ ] Clean commit history (squash messy commits if needed)
  - [ ] Push all code to `main` branch
  - [ ] Verify repo is public
  - [ ] Add demo video link to repo description
- [ ] Devpost Submission
  - [ ] Project name: FluentAI
  - [ ] Tagline: "The AI English coach that listens to you speak and makes you dangerously articulate"
  - [ ] Description: problem + solution + how it works + what makes it unique
  - [ ] Upload demo video (or link to YouTube/Loom)
  - [ ] Link to GitHub repo
  - [ ] Select prize categories: Best Use of ElevenLabs, Best Use of Gemini API
  - [ ] Tech stack tags
  - [ ] Screenshots
  - [ ] Submit before deadline
- [ ] Final Verification
  - [ ] Demo video plays correctly
  - [ ] GitHub repo is accessible (test with incognito browser)
  - [ ] README renders correctly on GitHub
  - [ ] Devpost submission is complete and published

**Done when:** Repo is public, README is polished, demo video is uploaded, Devpost submission is complete. Ship it. 🚀

---

_Every checkbox above is a concrete action. No checkbox requires guessing what to do. Complete them top-to-bottom and you arrive at a winning submission._
