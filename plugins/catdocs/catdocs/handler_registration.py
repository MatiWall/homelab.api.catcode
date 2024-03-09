from catdocs.event_bus import event_bus
from catdocs.events import EventType

from catdocs.handlers.startup import on_startup
from catdocs.handlers.mkdocs import build_docs, move_docs

event_bus.subscribe(EventType.ON_STARTUP, on_startup)

event_bus.subscribe(EventType.BUILD_DOCS, build_docs)
event_bus.subscribe(EventType.MOVE_DOCS, move_docs)