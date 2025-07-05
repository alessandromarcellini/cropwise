

class UsersRepository:
    # TODO the dicts will probably be replaced with SQLAlchemy models

    def __init__(self):
        pass

    def get_by_email(self, email: str):
        pass

    def create(self, user_data: dict):
        pass

    def authenticate(self, email: str, password: str):
        pass

    def deactivate(self, user_id: str):
        pass

class FarmFiledsRepository:
    # TODO the dicts will probably be replaced with SQLAlchemy models
    def __init__(self):
        pass

    def create(self, farm_field_data: dict):
        pass

    def get_by_station_id(self, station_id: int):
        pass

    def get_user_farm_fields(self, user_id: str):
        pass

    def get_by_id(self, farm_field_id: int):
        pass

class NotificationsRepository:
    # TODO the dicts will probably be replaced with SQLAlchemy models
    def __init__(self):
        pass

    def create(self, notification_data: dict):
        pass

    def get_by_farm_field(self, farm_field_id: int):
        pass