// ---- Speech DNA ----
export interface SpeechDNA {
  grammar: number;
  vocabulary: number;
  filler_words: number;
  sentence_complexity: number;
  idiom_usage: number;
  speaking_pace: number;
  coherence: number;
  confidence: number;
}

// ---- Lesson ----
export interface Lesson {
  id: string;
  user_id: string;
  title: string;
  status: "active" | "completed" | "abandoned";
  character: string;
  objectives: string[];
  created_at: string;
}

// ---- Analysis ----
export interface AnalysisResult {
  grammar_score: number;
  vocabulary_score: number;
  filler_count: number;
  sentence_complexity_score: number;
  idiom_score: number;
  pace_wpm: number;
  coherence_score: number;
  confidence_score: number;
  mistakes: Mistake[];
  missed_opportunities: MissedOpportunity[];
}

export interface Mistake {
  timestamp: string;
  original: string;
  correction: string;
  rule: string;
}

export interface MissedOpportunity {
  context: string;
  suggestion: string;
  type: "vocabulary" | "idiom" | "structure";
}

// ---- Report ----
export interface Report {
  lesson_id: string;
  overall_score: number;
  dimensions: SpeechDNA;
  key_moments: KeyMoment[];
  ghost_correction: GhostCorrection;
  ai_insight: string;
  future_you_audio_url?: string;
  xp_earned: number;
}

export interface KeyMoment {
  type: "great" | "fix" | "opportunity";
  quote: string;
  explanation: string;
}

export interface GhostCorrection {
  original: string;
  corrected: string;
  improvements: string[];
}

// ---- Roadmap ----
export interface RoadmapLevel {
  level: number;
  title: string;
  lessons: RoadmapLesson[];
  boss_battle?: RoadmapLesson;
}

export interface RoadmapLesson {
  id: string;
  title: string;
  description: string;
  status: "locked" | "available" | "completed";
  character: string;
  objectives: string[];
}

// ---- Gamification ----
export interface UserStats {
  xp: number;
  level: number;
  level_name: string;
  streak: number;
  achievements: Achievement[];
}

export interface Achievement {
  id: string;
  name: string;
  description: string;
  icon: string;
  unlocked_at?: string;
}

// ---- User ----
export interface User {
  id: string;
  name: string;
  goal: string;
  created_at: string;
}
