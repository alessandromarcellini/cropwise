from fastapi import APIRouter


router = APIRouter(
	prefix="/api/users",
	tags=["Users"],
)

@router.get("/")
async def root_endpoint():
    return {"message": "Users!"}