from pydantic import BaseModel


class SpeechDNASnapshot(BaseModel):
    grammar: float = 0
    vocabulary: float = 0
    filler_words: float = 0
    sentence_complexity: float = 0
    idiom_usage: float = 0
    speaking_pace: float = 0
    coherence: float = 0
    confidence: float = 0
