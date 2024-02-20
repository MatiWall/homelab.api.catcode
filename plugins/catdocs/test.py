import settings
from api.core.readers.github import GithubReader

from settings import config

# Replace 'your_access_token' with your GitHub personal access token
reader = GithubReader(token=config.github_token, username='MatiWall')

repos = reader.get_files()

for repo in repos:
    repo.fetch_zip(settings.BASE_DIR/'tmp')
