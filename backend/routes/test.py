from fastapi import APIRouter


router = APIRouter(
	prefix="/api/test",
	tags=["Testing"],
)

@router.get("/")
async def test_endpoint():
    return {"message": "Routing working!"}

