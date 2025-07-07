from fastapi import APIRouter
from routes.farm import router as farm_router
from routes.log import router as log_router
from routes.station import router as station_router
from routes.stations import router as stations_router
from routes.users import router as users_router

main_router = APIRouter()
main_router.include_router(farm_router)
main_router.include_router(log_router)
main_router.include_router(station_router)
main_router.include_router(stations_router)
main_router.include_router(users_router)