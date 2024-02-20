from pathlib import Path
from typing import Optional

from fastapi.exceptions import HTTPException

import yaml

from api.core.readers.github import GithubReader
from settings import BASE_DIR, config as app_config


class FilesystemDatabase:
    """
    A simple file system database class that stores data in YAML files.

    Parameters:
    - path (Path): The base directory where the YAML files are stored.

    Attributes:
    - path (Path): The base directory where the YAML files are stored.
    - cache (dict): A cache to store data retrieved from the file system.

    Methods:
    - get_all(): Retrieve all data from the file system.
    - get(id): Retrieve data for a specific ID, using the cache if available.
    - post(id, data): Insert or update data for a specific ID in the file system.
    - update(id, data): Update data for a specific ID in the file system.
    - delete(id): Delete data for a specific ID from the file system.
    """

    def __init__(self, path: Path):
        """
        Initialize the FilesystemDatabase with the specified base directory.

        Parameters:
        - path (Path): The base directory where the YAML files are stored.
        """
        self.path = path
        self.cache = self._get_all()

    def _get_all(self):
        """
        Retrieve all data from the file system.

        Returns:
        dict: A dictionary containing all data from the file system.
        """
        config = self._get(self.path / 'catcode-config.yaml')
        github_username = "MatiWall"
        github_token = app_config.github_token
        component_configs = GithubReader(username=github_username, token=github_token).get_files()
        data = {}
        for i, config in enumerate(component_configs):

            data[(
                config.metadata.system,
                config.metadata.application,
                config.metadata.deployable_unit)
            ] = config
        return data

    @staticmethod
    def _get(path):
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def get(self, id: Optional[tuple[str,str, str]] = None):
        """
        Retrieve data for a specific ID, using the cache if available.

        Parameters:
        - id (str): The ID for which to retrieve data.

        Returns:
        Any: The data associated with the specified ID, or None if not found.
        """
        if id is None:
            return list(self.cache.values())
        elif id in self.cache:
            return self.cache[id]
        elif id == 'new':
            return self._get(BASE_DIR / 'default_config/new.yaml')

        raise HTTPException(status_code=404, detail=f'File with id "{id}" does not exist')



    def stats(self):

        output_list = [list(item) for item in zip(*list(self.cache.keys()))]
        return {
            'applications': len(list(set(output_list[1]))),
            'systems': len(list(set(output_list[0]))),
            'deployableUnits': len(list(output_list[2]))
        }

