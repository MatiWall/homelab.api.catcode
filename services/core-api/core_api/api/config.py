import yaml
import settings
from fastapi import APIRouter


router = APIRouter(prefix='/config')
PATH = settings.BASE_DIR / 'catcode-config.yaml'
def read_yaml_file(file_path):
    with open(file_path, 'r') as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return data
@router.get('/')
def return_config():
    config = read_yaml_file(PATH)
    return config

@router.get('/{key}')
def return_config(key):
    config = read_yaml_file(PATH)
    return config[key]


