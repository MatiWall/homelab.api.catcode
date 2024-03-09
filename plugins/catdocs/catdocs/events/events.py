from enum import StrEnum

class EventType(StrEnum):
    ADDED_REPO = 'ADDED_REPO'
    UPDATED_REPO = 'UPDATED_REPO'
    DELETED_REPO = 'DELETED_REPO'
    ON_STARTUP = 'ON_STARTUP'
    BUILD_DOCS = 'BUILD_DOCS'
    MOVE_DOCS = 'MOVE_DOCS'

