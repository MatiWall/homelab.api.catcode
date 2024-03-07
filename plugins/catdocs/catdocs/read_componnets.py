import logging

logger = logging.getLogger(__name__)

import httpx
from catdocs.models import CatDocsComponent

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
                CatDocsComponent(
                    url=comp['metadata'].get('annotations', {}).get(config.catcode_url_annotation),
                    docs_path=comp['metadata'].get('annotations', {}).get(config.catdocs_path_annotation),
                    repo_path=comp['metadata'].get('annotations', {}).get(config.catcode_repo_path_annotation),
                    deployable_unit=comp['metadata']['deployableUnit'],
                    application=comp['metadata']['application'],
                    system=comp['metadata']['system']
                )
            )

    return comps
