from fastapi import APIRouter

router = APIRouter(prefix="/api/analysis", tags=["analysis"])


@router.get("/{lesson_id}")
async def get_analysis(lesson_id: str):
    # TODO: implement in P05
    return {"lesson_id": lesson_id, "analysis": {}}


@router.get("/{lesson_id}/report")
async def get_report(lesson_id: str):
    # TODO: implement in P05
    return {"lesson_id": lesson_id, "report": {}}
