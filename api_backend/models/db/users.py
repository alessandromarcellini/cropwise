from typing import List
from sqlalchemy import ForeignKey, SmallInteger, String, Table, Column, event
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from models.db.farm import FarmField
from models.db.logs import EntryLog

# from models.db.stations import Station

from core.orm import Base

starred_stations = Table(
    'starred_stations',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('station_id', ForeignKey('stations.id'), primary_key=True)
)

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)

    users: Mapped[List["User"]] = relationship(back_populates="role")

@event.listens_for(Role.__table__, 'after_create')
def create_default_roles(target, connection, **kw):
    # Insert default roles
    connection.execute(
        target.insert().values([
            {'name': 'admin'},
            {'name': 'farmer'},
            {'name': 'basic_user'},
        ])
    )
    connection.commit()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(30))
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    is_enabled: Mapped[bool]

    role_id: Mapped[int] = mapped_column(SmallInteger, ForeignKey("roles.id"))
    role: Mapped["Role"] = relationship(back_populates="users")

    farm_fields: Mapped[List["FarmField"]] = relationship(back_populates="user")
    entry_logs: Mapped[List["EntryLog"]] = relationship(back_populates="user")

    starred_stations: Mapped[List["Station"]] = relationship("Station", secondary="starred_stations", back_populates="starred_by")

    @validates('starred_stations')
    def validate_starred_stations_limit(self, key, starred_station):
        if len(self.starred_stations) >= 3:
            raise ValueError("A user can only star up to 3 weather stations.")
        return starred_station