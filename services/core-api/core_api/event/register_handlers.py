from core_api.event.event_bus import event_bus
from core_api.event.events import Events

from .handlers import (
    new_component,
    update_cache
)

event_bus.subscribe(Events.COMPONENT_CREATED, new_component)

event_bus.subscribe(Events.COMPONENT_UPDATED, update_cache)