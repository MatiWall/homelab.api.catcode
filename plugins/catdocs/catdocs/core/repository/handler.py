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
        if (self.base_path / comp.name).exists():
            self.reader.update(self.base_path / comp.name)
        else:
            self.reader.clone(comp, self.base_path/comp.name)
