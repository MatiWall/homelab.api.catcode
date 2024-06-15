import logging

from catdocs.utils import create_name

logger = logging.getLogger(__name__)

import httpx

from settings import config


async def read_components():
    logger.info('Reading componentes on startup')
    async with httpx.AsyncClient(follow_redirects=True, timeout=10) as client:
        resp = await client.get(config.core_api+'/catalog')

    if resp.status_code < 300:
        components = resp.json()['apps']
        logger.info(f'Successfully read {len(components)} components')
    else:
        logger.error(f'Failed to read catalog components with error: {resp.content}')
        raise Exception()

    comps = []

    for comp in components:
        if comp['metadata'].get('annotations', {}).get(config.catdocs_build_annotation):
            logger.debug(f'Successfully found catdocs annotation for component {create_name(comp)}')
            comps.append(
                comp
            )
        else:
            logger.debug(
                f'No catdocs annotation for component {create_name(comp)}')

    return comps
