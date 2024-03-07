from enum import Enum, auto
from pydantic import BaseModel

class EventType(Enum):
    ADDED_REPO = auto()
    UPDATED_REPO = auto()
    DELETED_REPO = auto()
    ON_STARTUP = auto()
    BUILD_DOCS = auto()

class Event(BaseModel):
    type: EventType
    body: object

