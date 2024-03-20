from messaging_tools import Message
from core_api.event.event_bus import event_bus
from core_api.event.queue import queue
from core_api.event.events import Events


async def service():
    on_startup_event = Message(
        type=Events.ON_START_UP
    )
    await event_bus.emit(on_startup_event)

    while True:
        # Wait for an event and process it
        event = await queue.get()
        await event_bus.emit(event)