import logging

from catdocs.core.events import EventType
from catdocs.core.events.message_broker import produce_message

logger = logging.getLogger(__name__)

import settings
from catdocs.cache import cache
from catdocs.tools import repo_handler
from catdocs.core.parser import create_component_from_object
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

    event = Message(
            type=EventType.DOCUMENTATION_DELETED
        )
    await produce_message(event)

    logger.info(f'Removed documentation for component {comp}')