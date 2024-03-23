from core_api.event.event_bus import event_bus
from core_api.event.events import Events

from .handlers import (
    on_start_up,
new_component,
update_cache,
externally_publish,
check_for_updates
)


event_bus.subscribe(Events.ON_START_UP, on_start_up)
event_bus.subscribe(Events.NEW_COMPONENT, new_component)

event_bus.subscribe(Events.UPDATED_COMPONENT, update_cache)
event_bus.subscribe(Events.UPDATED_COMPONENT, externally_publish)
event_bus.subscribe(Commands.LOOK_FOR_CHANGES, check_for_updates)