from typing import List
from controllers.persistance.stations import StationsRepository, StationRepository
from controllers.persistance.stations import SensorsRepository
from models.routes.stations import SensorState as SensorStateRoutesModel

class StationController:
    #station_id: int
    #persistance_controller: StationsRepository

    def __init__(self, station_id: int):
        self.station_id = station_id
        self.persistance_controller = StationRepository(station_id)
    
    # GETTERS ---------------------------------------------------
    
    def get_current_state(self) -> bool:
        return self.persistance_controller.get_state()

    def get_current_interval(self) -> float:
        return self.persistance_controller.get_interval()

    def get_sensors(self):
        return self.persistance_controller.get_sensors()

    def get_basic_data(self):
        return self.persistance_controller.get_basic_data()

    def get_data(self):
        data = self.persistance_controller.get_data()
        sensors = self.persistance_controller.get_sensors()
        return {
            **data,
            'sensors': sensors
        }

    # SETTERS ---------------------------------------------------
    def set_interval(self, new_interval: int):
        self.persistance_controller.set_interval(new_interval)

    def set_state(self, new_state: bool):
        self.persistance_controller.set_state(new_state)

    def get_number_of_viewing_users(self): # -> int
        # will be implemented using a websocket
        pass

    def get_associated_farmers(self):
        return self.persistance_controller.get_associated_farmers()

class SensorController:
    def __init__(self, sensor_id: int):
        self.sensor_id = sensor_id
        self.persistance_controller = SensorsRepository(sensor_id)
    
    def get_by_id(self):
        return self.persistance_controller.get_by_id()
    
    def set_sensor_state(self, station_id: int, new_state: bool):
        self.persistance_controller.set_state(station_id, new_state)
    


class UserStationController:
    #station_id: int

    def __init__(self, station_id: int):
        self.station_id = station_id

    # def get_current_data()-> List[Metric]: will not be used beacuse the data will be retrieved directly by te frontend using the firebase sdk
    #   pass

    # def get_past_data(self, start_date: str, end_date: str): # -> List[Metric]: same as above
    #     pass

    def add_to_starred(self, user_id: str): # user_id will be retrieved from the request context
        pass



class StationsController:
    #persistance_controller: StationsRepository
    def __init__(self):
        self.persistance_controller = StationsRepository()

    def get_stations(self): # -> List[Station]
        return self.persistance_controller.get_all()

    def find_stations(self, subname: str):
        return self.persistance_controller.filter_by_subname(subname)


def get_station_controller(station_id):
    controller = StationController(station_id)
    try:
        yield controller
    finally:
        controller.persistance_controller.close()

def get_sensor_controller(sensor_id):
    controller = SensorController(sensor_id)
    try:
        yield controller
    finally:
        controller.persistance_controller.close()