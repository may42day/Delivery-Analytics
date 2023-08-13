from enum import Enum
import enum
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Roles(enum.Enum):
    user = "USER"
    courier = "COURIER"


class RegistrationInfo(BaseModel):
    uuid: UUID
    role: Roles
    created_at: datetime


class RegCounter(BaseModel):
    date: str
    amount: int
