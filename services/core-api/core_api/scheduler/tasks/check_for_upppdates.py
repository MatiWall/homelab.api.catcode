from event_tools import Event
from core_api.event.events import Events
from core_api.event.queue import queue

async def emit_check_for_updates_event():
    event = Event(
        type=Events.LOOK_FOR_CHANGES
    )
    await queue.put(event)


