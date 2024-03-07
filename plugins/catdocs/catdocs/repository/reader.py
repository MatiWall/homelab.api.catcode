import os
import shutil
import subprocess
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class GitHub:
    @staticmethod
    def clone_url(item):
        repo_url = item.url

        # Extracting username and repository name from the URL
        username, repository = repo_url.split('/')[-2:]

        # Constructing the clone URL
        clone_url = f'https://github.com/{username}/{repository}.git'

        return clone_url

class GitHandler:
    def __init__(self):
        self.provider = GitHub()
    def clone(self, comp, output_dir: str):
        clone_url = self.provider.clone_url(comp)
        try:
            logger.debug(f"Cloning {clone_url} into {output_dir}")
            subprocess.run(['git', 'clone', clone_url, output_dir], check=True)

            logger.debug(f"Successfully cloned {clone_url} into {output_dir}")
        except Exception as e:
            logger.error(f"Failed to clone {clone_url} into {output_dir}: {e}")

    def update(self, path):
        # Repo exists, update it
        try:
            subprocess.run(['git', '-C', path, 'pull'])
        except subprocess.CalledProcessError as e:
            logger.exception(f"Failed to update repository at {path}")


