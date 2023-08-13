from enum import Enum


class QueueSatusType(Enum):
    completed = "completed"
    expired = "expired"
    canceled = "canceled"
