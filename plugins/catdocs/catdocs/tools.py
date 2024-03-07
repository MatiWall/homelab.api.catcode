from catdocs.repository.handler import RepoHandler
from catdocs.repository.reader import GitHandler
from catdocs.mkdocs import MKDocs
from settings import BASE_DIR

repo_handler = RepoHandler(
    base_path=BASE_DIR / 'tmp',
    reader=GitHandler()
)

mkdocs_handler = MKDocs(base_path=BASE_DIR / 'tmp')

