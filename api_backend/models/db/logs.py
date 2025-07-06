from datetime import datetime
from sqlalchemy import ForeignKey, SmallInteger, String, TIMESTAMP, BigInteger
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
    name: Mapped[str] = mapped_column(String(20), unique=True)