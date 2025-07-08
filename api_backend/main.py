from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.api import main_router

from core.orm import engine, Base

from models.db import stations, farm, logs, users 

from models.routes.stations import Interval

# Create FastAPI instance
app = FastAPI(
    title="CropWise",
    description="Backend API for CropWise application",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(main_router)
