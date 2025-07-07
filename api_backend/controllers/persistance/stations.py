from datetime import datetime
from core.PersistanceBase import PersistanceBase
from models.db.stations import Station, Sensor

from sqlalchemy import select

class StationRepository(PersistanceBase):
    #station_id : int
    
    def __init__(self, station_id: int):
        super().__init__()
        self.station_id = station_id

    def get_by_id(self):
        pass

    def get_all(self):
        pass

    def set_interval(self, interval: int):
        pass

    def set_state(self, state: bool):
        pass

    def get_associated_stations(self, farm_field_id: int):
        pass

class StationsRepository(PersistanceBase):
    def __init__(self):
        super().__init__()

    def filter_by_subname(self, station_subname: str):
        query = (
            select(
                Station.id,
                Station.name,
                Station.latitude,
                Station.longitude,
                Station.status,
            )
            .where(
                Station.name.ilike(f"{station_subname}%")
            )
        )
        result = self.session.execute(
            query
        )
        return result.mappings().all()

class MetricsRepository(PersistanceBase):
    def __init__(self):
        super().__init__()

    def get_by_id(self, metric_id: int):
        pass
    
    def get_in_timespan(self, station_id: int, start: datetime, end: datetime):
        pass

    def get_in_last_10_minutes(self, station_id: int):
        pass

class SensorsRepository(PersistanceBase):
    def __init__(self):
        super().__init__()

    def get_by_id(self, sensor_id: int):
        pass

    def set_state(self, sensor_id: int, state: bool):
        pass