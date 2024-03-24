import logging

from catdocs.events import EventType
from catdocs.tools import repo_handler

logger = logging.getLogger(__name__)

from catdocs.parser import create_component_from_object
from catdocs.queue import event_queue
from catdocs.cache import cache

from messaging_tools import Message

async def on_component_created_or_changed(event):

    body = event.body

    comp = create_component_from_object(body)
    # Update cache
    logger.debug('Updating cache on startup')
    cache.add(comp)
    logger.debug('Finished updating cache on startup')

    logger.info('Clone or update repositories')
    repo_handler.update_or_clone(comp)
    logger.info('Finished cloning or update repositories')

    await event_queue.put(
            Message(
                type=EventType.BUILD_DOCS,
                body=comp
            )
     )

