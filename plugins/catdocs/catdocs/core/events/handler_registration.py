from catdocs.core.events.event_bus import event_bus
from catdocs.core.events import EventType

from catdocs.core.events.handlers import on_component_created_or_changed, component_deleted

event_bus.subscribe(EventType.COMPONENT_UPDATED, on_component_created_or_changed)
event_bus.subscribe(EventType.COMPONENT_DELETED, component_deleted)
