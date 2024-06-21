import logging
logger = logging.getLogger(__name__)
from pathlib import Path

from catdocs.core.filesystem import rm_folder
from catdocs.core.repository.reader import GitHandler
class RepoHandler:
    def __init__(self, base_path: Path, reader: GitHandler):
        self.base_path = base_path
        self.reader = reader
    def delete(self, path: Path):
        rm_folder(path)
        return True

    def make_dir(self, path: Path):
        (self.base_path / path).mkdir(parents=True, exist_ok=True)

    def exists(self, path: Path):
        return (self.base_path / path).exists()

    def update_or_clone(self, comp):
        path = (self.base_path / comp.name)
        if path.exists():
            logger.debug(f'Pulling changes to existing repo {path}')
            self.reader.update(path)
        else:
            logger.debug(f'Cloning repo {path}')
            self.reader.clone(comp, path)
