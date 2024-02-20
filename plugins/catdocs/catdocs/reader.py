import os
import shutil
import subprocess
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class Repository(BaseModel):
    repo_url: str
    html_url: str
    branch: str
    name: str
    sha: str

    token: str

    def fetch_zip(self, clone_to):
        url = f'https://api.github.com/repos/MatiWall/{self.name}/zipball/'
        response = httpx.get(
            url,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": 'application/vnd.github.v3+json'
            },
            follow_redirects=True
        )

        if response.status_code == 200:
            zip_file_path = os.path.join(clone_to, f'{self.name}.zip')
            with open(zip_file_path, 'wb') as f:
                f.write(response.content)
            logger.debug(f"Zip file downloaded successfully as '{self.name}.zip'")

            # Extract the downloaded ZIP file using shutil
            shutil.unpack_archive(zip_file_path, clone_to)
            logger.debug(f"ZIP file extracted to '{clone_to}'")

            # Optionally, you can remove the downloaded ZIP file
            os.remove(zip_file_path)
            logger.debug(f"Downloaded ZIP file '{self.name}.zip' removed")
        else:
            logger.error(f"Failed to fetch zip file. Status code: {response.status_code}")
class GitHubReader:
    def __init__(self):
        pass
    def read(self, url: str, output_dir: str):
        try:
            logger.debug(f"Cloning {url} into {output_dir}")
            subprocess.run(['git', 'clone', url, output_dir], check=True)

            logger.debug(f"Successfully cloned {url} into {output_dir}")
        except Exception as e:
            logger.error(f"Failed to clone {url} into {output_dir}: {e}")

