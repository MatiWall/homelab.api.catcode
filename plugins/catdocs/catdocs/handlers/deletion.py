import logging

from catdocs.events import EventType

logger = logging.getLogger(__name__)

import settings
from catdocs.cache import cache
from catdocs.tools import repo_handler
from catdocs.parser import create_component_from_object
from catdocs.queue import event_queue
from messaging_tools import Message

async def component_deleted(event):
    comp = create_component_from_object(event.body)

    try:
        cache.remove(comp)
    except Exception as e:
        logger.exception(f"Failed to remove component {comp.name}: {e}")
        return False

    try:
        repo_handler.delete(settings.BASE_DIR / f'builds/{comp.name}')
    except Exception as e:
        logger.exception(f'Failed to delete documentation for {comp.name}: {e}')
        return False

    await event_queue.put(
        Message(
            type=EventType.DELETED_DOCUMENTATION
        )
    )

    logger.info(f'Removed documentation for component {comp}')