from fastapi import APIRouter

router = APIRouter(prefix="/api/profile", tags=["profile"])


@router.get("/{user_id}")
async def get_profile(user_id: str):
    # TODO: implement in P07
    return {"user_id": user_id, "xp": 0, "level": 1, "achievements": []}


@router.get("/{user_id}/dna")
async def get_speech_dna(user_id: str):
    # TODO: implement in P06
    return {"user_id": user_id, "dna": {}}
