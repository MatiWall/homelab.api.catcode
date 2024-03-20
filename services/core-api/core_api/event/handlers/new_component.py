import logging
logger = logging.getLogger(__name__)
from messaging_tools import Message

from core_api.core.componentcache import cache, tracked_paths
from core_api.event.events import Events
from core_api.event.queue import queue
async def new_component(event):

    logger.debug(f'Updating cache with {event.body}')
    status = tracked_paths.add(event.body)
    if status == 'Updated':
        event = Message(
            type=Events.UPDATED_COMPONENT,
            body=event.body
        )

    await queue.put(event)