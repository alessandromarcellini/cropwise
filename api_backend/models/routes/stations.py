from pydantic import BaseModel
from pydantic import field_validator

from enum import Enum, Flag

class StationState(Flag):
    active = True
    inactive = False

class SensorState(Flag):
    active = True
    inactive = False

class SensorType(str, Enum):
    humidity = "humidity"
    temperature = "temperature"
    pressure = "pressure"
    precipitation = "precipitation"
    # TODO add other sensor types

class Sensor(BaseModel):
    state: SensorState = SensorState.active
    sensor_type: SensorType

class BasicWeatherStation(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    state: StationState = StationState.active

    @field_validator("latitude")
    @classmethod
    def validate_latitude(cls, value):
        if not (-90 <= value <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        return value

    @field_validator("longitude")
    @classmethod
    def validate_longitude(cls, value):
        if not (-180 <= value <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        return value


class WeatherStation(BasicWeatherStation):
    misuration_interval: int = 500 # in milliseconds
    sensors: list[Sensor]
    
    @field_validator("misuration_interval")
    @classmethod
    def validate_longitude(cls, value):
        if not (250 <= value <= 5000):
            raise ValueError("Misuration interval must be between 0.25 and 5 seconds")
        return value
    
    @field_validator("sensors")
    @classmethod
    def validate_sensors_number(cls, value):
        if len(value) == 0:
            raise ValueError("A weather station must have at least one sensor")
        return value

class Metric(BaseModel):
    metric_type: SensorType
    value: float
