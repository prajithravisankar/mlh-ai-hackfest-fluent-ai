from fastapi import APIRouter

router = APIRouter(prefix="/api/lessons", tags=["lessons"])


@router.post("/start")
async def start_lesson():
    # TODO: implement in P04
    return {"lesson_id": "stub"}


@router.post("/{lesson_id}/end")
async def end_lesson(lesson_id: str):
    # TODO: implement in P04
    return {"lesson_id": lesson_id, "status": "completed"}


@router.get("/{lesson_id}")
async def get_lesson(lesson_id: str):
    # TODO: implement in P04
    return {"lesson_id": lesson_id}
