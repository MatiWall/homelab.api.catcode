import logging
logger = logging.getLogger(__name__)

from catdocs.cache import cache
from catdocs.tools import repo_handler
from catdocs.read_componnets import read_components
from catdocs.queue import event_queue
async def on_startup(event):

    components = await read_components()

    for component in components:
        event = Event(
            type=EventType.UPDATED_COMPONENT,
            body=component
        )
        await queue.put(event)


