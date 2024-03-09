import logging
logger = logging.getLogger(__name__)

import os
from pathlib import Path
import subprocess

class MKDocs:
    def __init__(self, base_path: Path):
        self.base_path = base_path

    def build(self, comp):
        """
           Run MkDocs on a given folder.

           Args:
               folder_path (str): The path to the folder containing MkDocs configuration file (mkdocs.yml).
           """
        try:
            folder_path = self.base_path / comp.name

            # Check if mkdocs.yml exists in the folder
            if not (folder_path / "mkdocs.yml").is_file():
                logger.info(f"Error: mkdocs.yml not found in {folder_path}.")
                return

            # Change directory to the folder path
            os.chdir(folder_path)
            # Run MkDocs build command
            output = subprocess.run(["mkdocs", "build"])
            if output.returncode == 0:
                logger.info("MkDocs build completed successfully.")
            else:
                raise Exception(f'Failed to generate documentation for {comp}.')
        except Exception as e:
            logger.exception(f"Failed to run MkDocs on folder: {folder_path}. Error: {e}")
            raise
