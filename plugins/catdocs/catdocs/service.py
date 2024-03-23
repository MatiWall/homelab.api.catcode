import asyncio
from event_tools import Event

from catdocs import event_bus
from catdocs.events import EventType
from catdocs.event_bus import event_bus
from catdocs.queue import event_queue


from settings import BASE_DIR

async def service():

    on_startup_event = Event(
        type=EventType.ON_STARTUP,
    )
    await event_bus.emit(on_startup_event)

    while True:
        # Wait for an event and process it
        event = await event_queue.get()
        await event_bus.emit(event)

