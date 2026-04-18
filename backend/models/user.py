from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str = ""
    goal: str = ""


class UserResponse(BaseModel):
    id: str
    name: str
    goal: str
    xp: int = 0
    level: int = 1
    streak: int = 0
    created_at: str
