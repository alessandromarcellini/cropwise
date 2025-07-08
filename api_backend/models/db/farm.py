from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey, SmallInteger, String, TIMESTAMP, Table, Column, event
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
    name: Mapped[str] = mapped_column(String(30), unique=True)
    hectares: Mapped[float]
    latitude: Mapped[float]
    longitude: Mapped[float]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="farm_fields")

    # cultivation_type_id: Mapped[int] = mapped_column(ForeignKey("cultivation_types.id"))
    # cultivation_type: Mapped["CultivationType"] = relationship(back_populates="farm_fields")

    plant_id: Mapped[int] = mapped_column(ForeignKey("plants.id"))
    plant: Mapped["Plant"] = relationship(back_populates="farm_fields")

    stations = relationship('Station', secondary=farmfield_stations_association, back_populates='farm_fields')

    @validates('stations')
    def validate_stations_limit(self, key, station):
        if len(self.stations) != 1 and len(self.stations) != 3:
            raise ValueError("A farm field can only be linked to 1 or 3 weather stations.")
        return station

    #TODO add triggers to restric latitude and longitude to valid values

class Plant(Base):
    __tablename__ = "plants"

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)

    cultivation_type_id: Mapped[int] = mapped_column(ForeignKey("cultivation_types.id"))

    farm_fields: Mapped[List["FarmField"]] = relationship(back_populates="plant")

@event.listens_for(Plant.__table__, 'after_create')
def create_default_cultivation_types(target, connection, **kw):
    # Insert default Plants
    connection.execute(
        target.insert().values([
            # High Irrigation (id = 1)
            {'name': 'Pomodori', 'cultivation_type_id': 1},
            {'name': 'Peperoni', 'cultivation_type_id': 1},
            {'name': 'Zucchine', 'cultivation_type_id': 1},
            {'name': 'Insalata', 'cultivation_type_id': 1},
            {'name': 'Cavoli', 'cultivation_type_id': 1},
            {'name': 'Agrumi', 'cultivation_type_id': 1},
            {'name': 'Fragole', 'cultivation_type_id': 1},
            {'name': 'Riso', 'cultivation_type_id': 1},
            {'name': 'Banane', 'cultivation_type_id': 1},

            # Medium Irrigation (id = 2)
            {'name': 'Mele', 'cultivation_type_id': 2},
            {'name': 'Pere', 'cultivation_type_id': 2},
            {'name': 'Pesche', 'cultivation_type_id': 2},
            {'name': 'Ciliegie', 'cultivation_type_id': 2},
            {'name': 'Uva', 'cultivation_type_id': 2},
            {'name': 'Piselli', 'cultivation_type_id': 2},
            {'name': 'Fagioli', 'cultivation_type_id': 2},
            {'name': 'Olive', 'cultivation_type_id': 2},
            {'name': 'Girasoli', 'cultivation_type_id': 2},
            {'name': 'Mais', 'cultivation_type_id': 2},

            # Low Irrigation (id = 3)
            {'name': 'Grano', 'cultivation_type_id': 3},
            {'name': 'Orzo', 'cultivation_type_id': 3},
            {'name': 'Segale', 'cultivation_type_id': 3},
            {'name': 'Avena', 'cultivation_type_id': 3},
            {'name': 'Tabacco', 'cultivation_type_id': 3},
            {'name': 'Cotone', 'cultivation_type_id': 3},
            {'name': 'Canapa', 'cultivation_type_id': 3},
            {'name': 'Caffè', 'cultivation_type_id': 3},
        ])
    )
    connection.commit()


class CultivationType(Base):
    __tablename__ = "cultivation_types"

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    days: Mapped[int] = mapped_column(SmallInteger)
    quantity: Mapped[float]

@event.listens_for(CultivationType.__table__, 'after_create')
def create_default_cultivation_types(target, connection, **kw):
    # Insert default cultivation types
    connection.execute(
        target.insert().values([
            {
                'name': 'AltaIrrigazione',
                'days': 2,
                'quantity': 75,
            },
            {
                'name': 'MediaIrrigazione',
                'days': 5,
                'quantity': 45,
            },
            {
                'name': 'BassaIrrigazione',
                'days': 15,
                'quantity': 15,
            },
        ])
    )
    connection.commit()


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str] = mapped_column(String(512))
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship()