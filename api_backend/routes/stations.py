from typing import List
from fastapi import APIRouter, Request, Depends
from models.routes.stations import BasicWeatherStation

from controllers.routes.weather_station import StationsController

router = APIRouter(
	prefix="/api/stations",
	tags=["Stations"],
)

@router.get("/")
async def get_stations(request: Request, controller: StationsController = Depends(StationsController)) -> List[BasicWeatherStation]:
    stations = controller.get_stations()
    return [BasicWeatherStation(**station) for station in stations]

@router.get("/find")
async def get_stations(request: Request, subname: str, controller: StationsController = Depends(StationsController)) -> List[BasicWeatherStation]:
    stations = controller.find_stations(subname)
    return [BasicWeatherStation(**station) for station in stations]
