import logging
logger = logging.getLogger(__name__)
from core_api.core.cache import cache
async def new_component(event):

    logger.debug(f'Updating cache with {event.body}')
    cache.add(event.body)