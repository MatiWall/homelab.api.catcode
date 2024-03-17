from pathlib import Path
from typing import Optional

from fastapi.exceptions import HTTPException

import yaml

from core_api.core.readers.github import GithubReader
from settings import BASE_DIR, config as app_config


class Cache:
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
        Initialize the Cache with the specified base directory.

        Parameters:
        - path (Path): The base directory where the YAML files are stored.
        """
        self.path = path
        self._cache = {}

    def add(self, component):
        self._cache[(
            component.metadata.system,
            component.metadata.application,
            component.metadata.deployable_unit)
        ] = component
        return True

    def get_all(self):
        """
        Retrieve all data from the file system.

        Returns:
        dict: A dictionary containing all data from the file system.
        """
        return self._cache

    def get(self, id: Optional[tuple[str,str, str]] = None):
        """
        Retrieve data for a specific ID, using the cache if available.

        Parameters:
        - id (str): The ID for which to retrieve data.

        Returns:
        Any: The data associated with the specified ID, or None if not found.
        """
        if id is None:
            return list(self._cache.values())
        elif id in self._cache:
            return self._cache[id]

        raise HTTPException(status_code=404, detail=f'File with id "{id}" does not exist')



    def stats(self):

        output_list = [list(item) for item in zip(*list(self._cache.keys()))]
        return {
            'applications': len(list(set(output_list[1]))),
            'systems': len(list(set(output_list[0]))),
            'deployableUnits': len(list(output_list[2]))
        }


cache = Cache(BASE_DIR)