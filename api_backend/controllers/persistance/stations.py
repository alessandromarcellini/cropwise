from datetime import datetime
from core.PersistanceBase import PersistanceBase
from models.db.stations import Station, Sensor, SensorType
from models.db.users import User
from models.db.farm import FarmField, farmfield_stations_association

from sqlalchemy import select, update

class StationRepository(PersistanceBase):
    #station_id : int
    
    def __init__(self, station_id: int):
        super().__init__()
        self.station_id = station_id

    def get_by_id(self):
        pass

    def get_interval(self):
        query = (
            select(Station.interval)
            .where(Station.id == self.station_id)
        )

        return self.session.execute(query).scalar_one()

    def set_interval(self, new_interval: int):
        update_query = (
            update(Station)
            .where(Station.id == self.station_id)
            .values(interval=new_interval)
        )
        self.session.execute(update_query)
        self.session.commit()

    def get_state(self):
        query = (
            select(Station.status)
            .where(Station.id == self.station_id)
        )

        return self.session.execute(query).scalar_one()

    def set_state(self, new_state: bool):
        update_query = (
            update(Station)
            .where(Station.id == self.station_id)
            .values(status=new_state)
        )
        self.session.execute(update_query)
        self.session.commit()

    def get_associated_stations(self, farm_field_id: int):
        pass

    def get_sensors(self):
        query = (
            select(
                Sensor.id,
                Sensor.status.label('state'),
                SensorType.type_name.label('sensor_type')
            )
            .join(SensorType, Sensor.type_id == SensorType.id)
            .where(Sensor.station_id == self.station_id)
        )

        return self.session.execute(query).mappings().all()
    
    def get_data(self):
        query = (
            select(
                Station.id,
                Station.name,
                Station.latitude,
                Station.longitude,
                Station.status.label('state'),
                Station.interval.label('misuration_interval'),
            )
            .where(Station.id == self.station_id)
        )
        return self.session.execute(query).mappings().one()
    
    def get_basic_data(self):
        query = (
            select(
                Station.id,
                Station.name,
                Station.latitude,
                Station.longitude,
                Station.status.label('state'),
            )
            .where(Station.id == self.station_id)
        )
        return self.session.execute(query).mappings().one()
    
    def get_associated_farmers(self):
        FARMER_ROLE_ID = 2
        query = (
            select(
                User.id,
                User.first_name.label('name'),
                User.last_name.label('surname'),
                User.email,
            ).distinct()
            .select_from(farmfield_stations_association)
            .join(FarmField, FarmField.id == farmfield_stations_association.c.farm_field_id)
            .join(User, User.id == FarmField.user_id)
            .where(
                farmfield_stations_association.c.station_id == self.station_id,
                User.role_id == FARMER_ROLE_ID, # shouldn't be necessary but won't hurt
                User.id == FarmField.user_id
            )
        )
        return self.session.execute(query).mappings().all()

class StationsRepository(PersistanceBase):
    def __init__(self):
        super().__init__()
    
    def get_all(self):
        query = (
            select(
                Station.id,
                Station.name,
                Station.latitude,
                Station.longitude,
                Station.status,
            )
        )
        result =  self.session.execute(query)
        return result.mappings().all()

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
    def __init__(self, sensor_id: int):
        super().__init__()
        self.sensor_id = sensor_id

    def get_by_id(self):
        query = (
            select(
                Sensor.id,
                Sensor.status.label('state'),
                SensorType.type_name.label('sensor_type')
            )
            .join(SensorType, Sensor.type_id == SensorType.id)
            .where(Sensor.id == self.sensor_id)
        )
        result = self.session.execute(query).mappings().one_or_none()
        if not result:
            raise ValueError("Sensor doesn't exist")
        return result
            

    def set_state(self, station_id: int, new_state: bool):
        real_station_id_query = (
            select(
                Sensor.station_id
            )
            .where(
                Sensor.id == self.sensor_id
            )
        )

        real_station_id = self.session.execute(real_station_id_query).scalar()
        if real_station_id != station_id:
            raise ValueError("The selected sensor doesn't belong to the selected station.")

        update_query = (
            update(Sensor)
            .where(Sensor.id == self.sensor_id)
            .values(status=new_state)
        )
        self.session.execute(update_query)
        self.session.commit()