import logging

from core_api.core.componentcache import tracked_paths, cache
from core_api.core.reader.models import CatCodeRepoEntry

logger = logging.getLogger(__name__)
from core_api.core.reader import repo_reader

async def on_start_up():
    logger.info('Reading components on startup and creating COMPONENT_CREATED events for initialization.')
    repos = repo_reader.files()


    for repo in repos:
        logger.debug(f'Updating tracked components with {repo}')
        status = tracked_paths.add(repo)

        logger.debug(f'Updating cache with component {repo}')
        component = repo_reader.get_file_content(repo)
        cache.add(component)