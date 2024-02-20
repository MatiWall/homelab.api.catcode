import httpx
from settings import config

def read_configs():
    resp = httpx.get(config.backend_url + '/catalog', follow_redirects=True)

    if resp.status_code < 300:

        apps = resp.json()['apps']


        return {(app["metadata"]["system"],app["metadata"]["application"],app["metadata"]["deployableUnit"]): app for app in apps}

    return {}
