import logging
logger = logging.getLogger(__name__)

from catdocs.cache import cache
from catdocs.tools import repo_handler

async def on_startup(event):

    # Update cache
    logger.debug('Updating cache on startup')
    for comp in event.body:
        cache.add(comp)
    logger.debug('Finished updating cache on startup')

    logger.info('Clone or update repositories')
    for comp in event.body:
        repo_handler.update_or_clone(comp)
    logger.info('Finished cloning or update repositories')


