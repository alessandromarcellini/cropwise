from fastapi import APIRouter, Request, Depends

from controllers.routes.weather_station import StationsController

router = APIRouter(
	prefix="/api/stations",
	tags=["Stations"],
)

@router.get("/")
async def get_stations(request: Request):
    return {"message": "List of stations"}

@router.get("/find")
async def get_stations(request: Request, subname: str, controller: StationsController = Depends(StationsController)):
    return controller.find_stations(subname)

