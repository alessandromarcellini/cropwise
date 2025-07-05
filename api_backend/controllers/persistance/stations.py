from datetime import datetime

class StationsRepository:
    def __init__(self):
        pass

    def get_by_id(self, station_id: int):
        pass

    def get_all(self):
        pass

    def filter_by_subname(self, station_subname: str):
        pass

    def get_starred_stations(self, user_id: int):
        pass

    def get_associated_stations(self, farm_field_id: int):
        pass

    def set_interval(self, station_id: int, interval: int):
        pass

    def set_state(self, station_id: int, state: bool):
        pass

class MetricsRepository:
    def __init__(self):
        pass

    def get_by_id(self, metric_id: int):
        pass
    
    def get_in_timespan(self, station_id: int, start: datetime, end: datetime):
        pass

    def get_in_last_10_minutes(self, station_id: int):
        pass

class SensorsRepository:
    def __init__(self):
        pass

    def get_by_id(self, sensor_id: int):
        pass

    def set_state(self, sensor_id: int, state: bool):
        pass