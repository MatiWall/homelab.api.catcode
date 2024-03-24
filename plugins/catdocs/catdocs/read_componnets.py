import logging

logger = logging.getLogger(__name__)

import httpx

from settings import config


async def read_components():

    async with httpx.AsyncClient(follow_redirects=True) as client:
        resp = await client.get(config.core_api+'/catalog')

    if resp.status_code < 300:
        components = resp.json()['apps']
    else:
        logger.error(f'Failed to read catalog components with error: {resp.content}')
        raise Exception()

    comps = []

    for comp in components:
        if comp['metadata'].get('annotations', {}).get(config.catdocs_build_annotation):

            comps.append(
                comp
            )

    return comps
