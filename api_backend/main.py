from fastapi import FastAPI
from routers.api import main_router

from core.orm import engine, Base

from models.db import stations, farm, logs, users 

# Create FastAPI instance
app = FastAPI(
    title="CropWise",
    description="Backend API for CropWise application",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(main_router)
