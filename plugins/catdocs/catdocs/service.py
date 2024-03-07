import asyncio

from catdocs import event_bus
from catdocs.events import Event, EventType
from catdocs.event_bus import event_bus
from catdocs.queue import event_queue
from catdocs.read_componnets import read_components


from settings import BASE_DIR

async def service():
    components = await read_components()

    on_startup_event = Event(
        type=EventType.ON_STARTUP,
        body=components
    )
    await event_bus.publish(on_startup_event)
    await event_bus.publish(
        Event(
            type=EventType.BUILD_DOCS,
            body=components[0]
        )
    )

    while True:
        # Wait for an event and process it
        event = await event_queue.get()
        await event_bus.publish(event)

