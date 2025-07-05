from pydantic import BaseModel, Field

from datetime import datetime, timezone

from models.routes.users import User
from models.routes.stations import Metric

from enum import Enum

class LogEntry(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ActionType(str, Enum):
    view_current_weather = "view_current_weather"
    view_past_weather = "view_past_weather"
    login = "login"
    failed_login = "failed_login"
    logout = "logout"
    signup = "signup"
    #TODO add more actions as needed

class OperationLog(LogEntry):
    user: User
    action: ActionType

class WeaterStationLog(LogEntry):
    station_id: int
    metric: Metric
