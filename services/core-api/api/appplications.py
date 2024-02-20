from pydantic import BaseModel
from fastapi import APIRouter

from api.core.file_database import FilesystemDatabase
from api.core.models import Metadata, Application
from settings import BASE_DIR

router = APIRouter(prefix='/catalog')

path = BASE_DIR
database = FilesystemDatabase(path)


class ApplicationCatalog(BaseModel):
    apps: list[Metadata]

class Applications(BaseModel):
    apps: list[Application]

@router.get('/')
def get_applications():
    configs = database.get()

    apps = []
    for config in configs:
        apps.append(config)

    return Applications(apps=apps)


@router.get('/component/{system}/{application}/{deployableunit}')
def get_applications(system: str, application: str, deployableunit: str):
    config = database.get((system, application, deployableunit))

    return config
