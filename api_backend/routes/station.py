from typing import List
from fastapi import APIRouter, Request, Depends, Body

from controllers.routes.weather_station import StationController, SensorController, get_station_controller, get_sensor_controller

from models.routes.stations import Sensor, WeatherStation, BasicWeatherStation, Interval, StationState, SensorState 
from models.routes.users import User

router = APIRouter(
	prefix="/api/station",
	tags=["Station"],
)

@router.get("/{station_id}")
async def root(station_id: int, request: Request, controller: StationController = Depends(get_station_controller)) -> WeatherStation:
    station = controller.get_data()
    return WeatherStation(**station)

@router.get("/{station_id}/currentState")
async def get_current_state(station_id: int, request: Request, controller: StationController = Depends(get_station_controller)) -> bool:
    return controller.get_current_state()

@router.get("/{station_id}/currentInterval")
async def get_current_interval(station_id: int, request: Request, controller: StationController = Depends(get_station_controller)) -> float:
    return controller.get_current_interval()

@router.get("/{station_id}/sensors")
async def get_sensors(station_id: int, request: Request, controller: StationController = Depends(get_station_controller)) -> List[Sensor]:
    sensors = controller.get_sensors()
    return [Sensor(**sensor) for sensor in sensors]

@router.get("/{station_id}/basicData")
async def get_basic_data(station_id: int, request: Request, controller: StationController = Depends(get_station_controller)):
    station_data = controller.get_basic_data()
    return BasicWeatherStation(**station_data)

@router.get("/{station_id}/numberOfViewingUsers")
async def get_number_of_viewing_users(station_id: int, request: Request, controller: StationController = Depends(get_station_controller)):
    return {"message": "This will not be implemented right away (probably never)"}

@router.get("/{station_id}/associatedFarmers")
async def get_associated_farmers(station_id: int, request: Request, controller: StationController = Depends(get_station_controller)) -> List[User]:
    farmers = controller.get_associated_farmers()
    return [User(**farmer) for farmer in farmers]

# POST ----------------------------------

@router.post("/{station_id}/setInterval")
async def set_interval(station_id: int, request: Request, new_interval: Interval, controller: StationController = Depends(get_station_controller)):
    #TODO forward the call to the iot_backend that will dispatch it to the corresponding station. If success => update the value in the db
    
    controller.set_interval(new_interval.value)
    return {"message": f"Interval Updated Successfully to {new_interval.value}"}

@router.post("/{station_id}/setState")
async def set_state(station_id: int, new_state: StationState, request: Request, controller: StationController = Depends(get_station_controller)):
    #TODO forward the call to the iot_backend that will dispatch it to the corresponding station. If success => update the value in the db
    
    controller.set_state(new_state.to_bool())
    return {"message": f"Station State Updated Successfully to {new_state.value}"}

@router.post("/{station_id}/sensor/{sensor_id}/setState")
async def set_sensor_state(station_id: int, sensor_id: int, new_state: SensorState, request: Request, controller: SensorController = Depends(get_sensor_controller)):
    #TODO forward the call to the iot_backend that will dispatch it to the corresponding station. If success => update the value in the db
    
    controller.set_sensor_state(station_id, new_state.to_bool())
    return {"message": f"Sensor State Updated Successfully to {new_state.value}"}

@router.get("/{station_id}/sensor/{sensor_id}/")
async def get_sensor(station_id: int, sensor_id: int, request: Request, controller: SensorController = Depends(get_sensor_controller)):
    sensor = controller.get_by_id()
    return Sensor(**sensor)