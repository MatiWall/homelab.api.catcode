from catdocs.event_bus import event_bus
from catdocs.events import EventType

from catdocs.handlers.startup import on_startup
from catdocs.handlers.mkdocs import build_docs, move_docs
from catdocs.handlers.changes import on_component_created_or_changed

event_bus.subscribe(EventType.ON_STARTUP, on_startup)
event_bus.subscribe(EventType.UPDATED_COMPONENT, on_component_created_or_changed)

event_bus.subscribe(EventType.BUILD_DOCS, build_docs)
event_bus.subscribe(EventType.MOVE_DOCS, move_docs)