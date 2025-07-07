from typing import List
from controllers.persistance.stations import StationsRepository, StationRepository

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
        pass

    def get_data(self):
        data = self.persistance_controller.get_data()
        sensors = self.persistance_controller.get_sensors()
        return {
            **data,
            'sensors': sensors
        }

    # SETTERS ---------------------------------------------------
    def set_interval(self, interval: float):
        pass

    def set_sensor_state(self, sensor_id: int, state: bool):
        pass

    def set_state(self, state: bool):
        pass

    def get_number_of_viewing_users(self): # -> int
        # will be implemented using a websocket
        pass

    def get_associated_farmers(self): # -> List[Farmer]
        pass


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