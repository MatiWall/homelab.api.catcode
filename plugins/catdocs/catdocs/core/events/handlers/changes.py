import logging

from settings import config

logger = logging.getLogger(__name__)

from messaging_tools import Message

from catdocs.tools import repo_handler, mkdocs_handler



from catdocs.core.parser import create_component_from_object
from catdocs.cache import cache



async def on_component_created_or_changed(event: Message):
    logger.info(f'Component was created or changed: {event.body}')
    entity = event.body
    comp = create_component_from_object(entity)
    # Update cache
    logger.debug('Updating cache')
    cache.add(comp)

    logger.info('Clone or update repositories')
    repo_handler.update_or_clone(comp)
    logger.info('Finished cloning or update repositories')

    if entity['metadata'].get('annotations', {}).get(config.catdocs_build_docs_folder_annotation):
        mkdocs_handler.create_docs(comp)

    mkdocs_handler.create_mkdocs_config_if_not_exists(comp)

    logger.info(f'Building documentation for component {comp}.')
    mkdocs_handler.build(comp)

    logger.info(f'moving documentation for component {comp} into builds folder.')
    mkdocs_handler.move_docs(comp)

