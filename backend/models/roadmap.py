from pydantic import BaseModel


class RoadmapLesson(BaseModel):
    id: str
    title: str
    description: str
    status: str = "locked"
    character: str = ""
    objectives: list[str] = []


class RoadmapLevel(BaseModel):
    level: int
    title: str
    lessons: list[RoadmapLesson] = []
    boss_battle: RoadmapLesson | None = None
