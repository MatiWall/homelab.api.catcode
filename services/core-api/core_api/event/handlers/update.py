import logging
logger = logging.getLogger(__name__)

from core_api.core.cache import cache


async def check_for_updates(event):
    print(f'implement check for updates in {__file__}')

async def update_cache(event):
    logger.debug(f'Updating cache with component {event.body}')
    cache.add(event.body)


async def externally_publish(event):
    print('Submit to rabbitmq')
