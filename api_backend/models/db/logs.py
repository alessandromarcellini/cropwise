from datetime import datetime
from sqlalchemy import ForeignKey, SmallInteger, String, TIMESTAMP, BigInteger, event
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.orm import Base

# from models.db.users import User
# from models.db.stations import Station

class EntryLog(Base):
    __tablename__ = "entry_logs"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="entry_logs")

    station_id: Mapped[int] = mapped_column(ForeignKey("stations.id"))
    # TODO station: Mapped["Station"] = relationship()

    operation_type_id: Mapped[int] = mapped_column(ForeignKey("operation_types.id"))
    operation_type: Mapped["OperationType"] = relationship()


class OperationType(Base):
    __tablename__ = "operation_types"

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)

@event.listens_for(OperationType.__table__, 'after_create')
def create_default_cultivation_types(target, connection, **kw):
    # Insert default Operation Types
    connection.execute(
        target.insert().values([
            {'name': 'login'},
            {'name': 'registration'},
            {'name': 'metric_received'},
            {'name': 'changed_interval'},
            {'name': 'changed_station_state'},
            {'name': 'changed_sensor_state'},
            {'name': 'realtime_data'},
            {'name': 'past_data'},
            {'name': 'starred_station'},
        ])
    )
    connection.commit()
