from fastapi import APIRouter


router = APIRouter(
	prefix="/api/farm",
	tags=["Farm"],
)

@router.get("/")
async def root_endpoint():
    return {"message": "Farm!"}