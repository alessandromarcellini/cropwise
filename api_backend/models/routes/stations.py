from pydantic import BaseModel
from pydantic import field_validator

from enum import Enum

class StationState(str, Enum):
    active = "active"
    inactive = "inactive"

    def to_bool(self) -> bool:
        return self == StationState.active

class SensorState(str, Enum):
    active = "active"
    inactive = "inactive"

    def to_bool(self) -> bool:
        return self == SensorState.active
    
    def to_state(bool_value: bool):
        if bool_value:
            return SensorState.active
        return SensorState.inactive

class SensorType(str, Enum):
    air_humidity = "air_humidity"
    ground_humidity = "ground_humidity"
    temperature = "temperature"
    pressure = "pressure"
    precipitation = "precipitation"
    wind = "wind"
    cloud_presence = "cloud_presence"
    # TODO add other sensor types

class Sensor(BaseModel):
    id: int
    state: SensorState = SensorState.active
    sensor_type: SensorType

    @field_validator('state', mode='before')
    @classmethod
    def validate_state(cls, v):
        if isinstance(v, bool):
            return 'active' if v else 'inactive'
        return v
    
    @field_validator('sensor_type', mode='before')
    @classmethod
    def validate_sensor_type(cls, v):
        if hasattr(v, 'value'):
            return v.value
        return v

class BasicWeatherStation(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    state: StationState = StationState.active

    @field_validator('state', mode='before')
    @classmethod
    def validate_state(cls, v):
        if isinstance(v, bool):
            return 'active' if v else 'inactive'
        return v

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
    def validate_misuration_interval(cls, value):
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


# ------------ POST REQUESTS MODELS --------------------------
class Interval(BaseModel):
    value: int
    
    @field_validator("value")
    @classmethod
    def validate_misuration_interval(cls, value):
        if not (250 <= value <= 5000):
            raise ValueError("Misuration interval must be between 0.25 and 5 seconds")
        return value

class StatePayload(BaseModel):
    new_state: StationState

    def to_bool(self) -> bool:
        return self.new_state == SensorState.active