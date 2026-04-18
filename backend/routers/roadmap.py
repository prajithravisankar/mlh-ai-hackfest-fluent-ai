from fastapi import APIRouter

router = APIRouter(prefix="/api/roadmap", tags=["roadmap"])


@router.get("/{user_id}")
async def get_roadmap(user_id: str):
    # TODO: implement in P08
    return {"user_id": user_id, "levels": []}
