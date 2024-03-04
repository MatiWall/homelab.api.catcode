from fastapi import APIRouter

from dependecies.reader import read_configs

router = APIRouter(prefix='/dependencies')
def dependency(configs, identifier: str = None):
    if identifier is not None:
        name = identifier.split('.')
        value = configs[(name[0], name[1], name[2])]
        entry = {
            'system': name[0],
            'application': name[1],
            'deployableUnit': name[2],
            'dependencies': [configs[(dep.split('.')[0], dep.split('.')[1], dep.split('.')[2])]['metadata']['uid'] for dep in value['spec'].get('dependencies', [])],
            'id': value['metadata']['uid']
        }
        return [entry]
    data = []
    for name, values in configs.items():
        entry = {
            'system': name[0],
            'application': name[1],
            'deployableUnit': name[2],
            'dependencies': [configs[(dep.split('.')[0], dep.split('.')[1], dep.split('.')[2])]['metadata']['uid'] for dep in values['spec'].get('dependencies', [])],
            'id': values['metadata']['uid']
        }
        data.append(entry)
    return data


@router.get('/')
def get_application_dependency():
    configs = read_configs()

    dep = dependency(configs)

    return dep
@router.get('/{system}/{application}/{deployableunit}')
def get_application_dependency(system: str, application: str, deployableunit: str):
    configs = read_configs()

    dep = dependency(configs, identifier=f'{system}.{application}.{deployableunit}')

    return dep