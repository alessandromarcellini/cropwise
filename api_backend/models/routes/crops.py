from pydantic import BaseModel, Field
from pydantic import field_validator
from typing import List

from datetime import datetime, timezone

from enum import Enum

from models.routes.stations import WeatherStation

class CropType(str, Enum):
    high_irrigation = "high_irr"
    medium_irrigation = "medium_irr"
    low_irrigation = "low_irr"

class CropName(str, Enum):
    apple = "apple"
    mais = "mais"
    olive = "olive"
    wheat = "wheat"
    #TODO add the other crops

class FarmField(BaseModel):
    id: int | None = None
    # farmer: Farmer circular import, not sure it will ever be needed
    crop_type: CropType
    crop_name: CropName
    size: float
    latitude: float
    longitude: float
    last_watered: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    reference_stations: List[WeatherStation] = []

    @field_validator('reference_stations')
    @classmethod
    def max_starred_stations(cls, value):
        if len(value) > 3:
            raise ValueError("A field can only reference up to 3 weather stations")
        return value
    
    @field_validator("latitude")
    @classmethod
    def validate_latitude(cls, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        return value

    @field_validator("longitude")
    @classmethod
    def validate_longitude(cls, value):
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        return value