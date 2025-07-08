from pydantic import BaseModel, EmailStr
from pydantic import field_validator
from typing import List

from models.routes.crops import FarmField

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    hashed_password: str | None = None
    is_active: bool | None = None

    # @field_validator('password')
    # @classmethod
    # def password_length(cls, value):
    #     if len(value) < 8:
    #         raise ValueError("Password must be at least 8 characters long")
    #     return value

class NonAdminUser(User):
    starred_stations: List[str] = []
    
    @field_validator('starred_stations')
    @classmethod
    def max_starred_stations(cls, value):
        if len(value) > 3:
            raise ValueError("You can only star up to 3 stations")
        return value

class Farmer(NonAdminUser):
    crops: List[FarmField] = []
class BasicUser(NonAdminUser):
    pass