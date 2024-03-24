import logging

from catdocs.core.events import EventType
from catdocs.tools import repo_handler, mkdocs_handler

logger = logging.getLogger(__name__)

from catdocs.core.parser import create_component_from_object
from catdocs.cache import cache



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

    mkdocs_handler.build(comp)
    mkdocs_handler.move_docs(comp)

