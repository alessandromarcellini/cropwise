from typing import List
from sqlalchemy import ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.db.farm import farmfield_stations_association

from core.orm import Base

class Station(Base):
    __tablename__ = "stations"

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    latitude: Mapped[float]
    longitude: Mapped[float]
    status: Mapped[bool]
    interval: Mapped[int] = mapped_column(SmallInteger)
    hashed_token: Mapped[str] = mapped_column(String(100))

    sensors: Mapped[List["Sensor"]] = relationship(back_populates="station")
    
    farm_fields = relationship('FarmField', secondary=farmfield_stations_association, back_populates='stations')
    starred_by = relationship("User", secondary="starred_stations", back_populates="starred_stations")

class Sensor(Base):
    __tablename__ = "sensors"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[bool]

    station_id: Mapped[int] = mapped_column(ForeignKey("stations.id"))
    station: Mapped["Station"] = relationship(back_populates="sensors")

    type_id: Mapped[int] = mapped_column(ForeignKey("sensor_types.id"))
    sensor_type: Mapped["SensorType"] = relationship(back_populates="sensors")


class SensorType(Base):
    __tablename__ = "sensor_types"

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    type_name: Mapped[str] = mapped_column(String(20), unique=True)

    sensors: Mapped[List["Sensor"]] = relationship(back_populates="sensor_type")