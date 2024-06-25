import logging
logger = logging.getLogger(__name__)

import httpx
from settings import config

def read_configs():
    url = config.backend_url + '/catalog'
    logger.info(f'Reading catalog entities from {url}')
    resp = httpx.get(url, follow_redirects=True)

    if resp.status_code < 300:
        apps = resp.json()['apps']
        logger.debug(f'Successfully read {len(apps)} catalog entities.')



        return {(app["metadata"]["system"],app["metadata"]["application"],app["metadata"]["deployableUnit"]): app for app in apps}
    logger.error(f'Failed to read catalog entities with status {resp.status_code}: \n\n {resp.content}')

    return {}
