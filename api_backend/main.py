from fastapi import FastAPI
from routers.api import main_router

# Create FastAPI instance
app = FastAPI(
    title="CropWise",
    description="Backend API for CropWise application",
    version="1.0.0"
)

app.include_router(main_router)
