from pydantic import BaseModel


class LessonStart(BaseModel):
    user_id: str
    character: str = "coach_alex"
    objectives: list[str] = []


class LessonResponse(BaseModel):
    id: str
    user_id: str
    title: str
    character: str
    status: str
    objectives: list[str]
    created_at: str
