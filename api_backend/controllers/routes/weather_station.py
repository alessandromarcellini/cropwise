
class StationController:
    #station_id: int

    def __init__(self, station_id: int):
        self.station_id = station_id
    
    # GETTERS ---------------------------------------------------
    
    def get_current_state(self): # -> StationState
        pass

    def get_current_interval(self): # -> float
        pass

    def get_sensors(self): # -> List[Sensor]
        pass

    def get_basic_data(self): # -> StationBasicData
        pass

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
    def __init__(self):
        pass

    def get_stations(self): # -> List[Station]
        pass

    def find_stations(self, subname: str): # -> List[Station]
        pass

    