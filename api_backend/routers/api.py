from fastapi import APIRouter
from routes.test import router as test_router

main_router = APIRouter()
main_router.include_router(test_router)