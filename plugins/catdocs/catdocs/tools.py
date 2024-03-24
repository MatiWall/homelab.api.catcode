from catdocs.core.repository.handler import RepoHandler
from catdocs.core.repository.reader import GitHandler
from catdocs.core.mkdocs import MKDocs
from settings import BASE_DIR

repo_handler = RepoHandler(
    base_path=BASE_DIR / 'tmp',
    reader=GitHandler()
)

mkdocs_handler = MKDocs(base_path=BASE_DIR / 'tmp')

