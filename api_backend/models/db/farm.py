from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey, SmallInteger, String, TIMESTAMP, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

# from models.db.users import User

from core.orm import Base


farmfield_stations_association = Table(
    'farmfield_stations_association',
    Base.metadata,
    Column('farm_field_id', ForeignKey('farm_fields.id'), primary_key=True),
    Column('station_id', ForeignKey('stations.id'), primary_key=True)
)

class FarmField(Base):
    __tablename__ = "farm_fields"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    hectares: Mapped[float]
    latitude: Mapped[float]
    longitude: Mapped[float]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="farm_fields")

    cultivation_type_id: Mapped[int] = mapped_column(ForeignKey("cultivation_types.id"))
    cultivation_type: Mapped["CultivationType"] = relationship(back_populates="farm_fields")

    plant_id: Mapped[int] = mapped_column(ForeignKey("plants.id"))
    plant: Mapped["Plant"] = relationship(back_populates="farm_fields")

    stations = relationship('Station', secondary=farmfield_stations_association, back_populates='farm_fields')

    @validates('stations')
    def validate_stations_limit(self, key, station):
        if len(self.stations) != 1 and len(self.stations) != 3:
            raise ValueError("A farm field can only be linked to 1 or 3 weather stations.")
        return station

    #TODO add triggers to restric latitude and longitude to valid values

class CultivationType(Base):
    __tablename__ = "cultivation_types"

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)
    days: Mapped[int] = mapped_column(SmallInteger)
    quantity: Mapped[float]

    farm_fields: Mapped[List["FarmField"]] = relationship(back_populates="cultivation_type")


class Plant(Base):
    __tablename__ = "plants"

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True)

    farm_fields: Mapped[List["FarmField"]] = relationship(back_populates="plant")


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str] = mapped_column(String(512))
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship()