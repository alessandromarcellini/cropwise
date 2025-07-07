from fastapi import APIRouter


router = APIRouter(
	prefix="/api/log",
	tags=["Logs"],
)

@router.get("/")
async def root_endpoint():
    return {"message": "Logs!"}
