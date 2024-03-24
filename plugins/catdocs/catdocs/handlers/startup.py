import logging

from catdocs.events import EventType

logger = logging.getLogger(__name__)

from catdocs.read_componnets import read_components
from catdocs.queue import event_queue
from messaging_tools import Message
async def on_startup(event):

    components = await read_components()

    for component in components:
        event = Message(
            type=EventType.UPDATED_COMPONENT,
            body=component
        )
        await event_queue.put(event)


