import logging

import settings
from catdocs.core.filesystem import rm_folder

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

    @staticmethod
    def move_docs(comp):
        initial_path = settings.BASE_DIR / f'tmp/{comp.name}/site'
        final_path = settings.BASE_DIR / f'builds/{comp.name}/site'

        logger.debug(f'Moving {comp.name} from {initial_path} to {final_path}')

        # Create the build directory if it doesn't exist
        final_path.parent.mkdir(parents=True, exist_ok=True)

        # Check if file already exists in final location and delete it if it does
        if final_path.exists():
            try:
                rm_folder(final_path)
                logger.debug(f'Removed existing file at {final_path}')
            except Exception as e:
                logger.exception(f'Failed to remove existing file at {final_path}: {e}')
                return  # Stop execution if deletion fails

        # Move the file
        try:
            path = Path(initial_path)
            path.rename(final_path)
            logger.debug(f'Successfully moved {comp.name} from {initial_path} to {final_path}')
        except Exception as e:
            logger.exception(f'Failed to move {comp.name} from {initial_path} to {final_path}: {e}')
