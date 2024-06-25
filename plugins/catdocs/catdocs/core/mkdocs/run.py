import logging
import ast
import shutil

import yaml
import settings
from catdocs.core.filesystem import rm_folder
from catdocs.models import CatDocsComponent

logger = logging.getLogger(__name__)

import os
from pathlib import Path
import subprocess


class MKDocs:
    def __init__(self, base_path: Path):
        self.base_path = base_path

    def default_config(self, comp):
        config_data = {
            'site_name': comp.name.replace('.', ' ').title(),
            'plugins': [
                'search',
                {
                    'mkdocstrings': {
                        'default_handler': 'python',
                        'handlers': {
                            'python': {
                                'options': {
                                    'show_source': True,
                                    'docstring_style': 'numpy'
                                }
                            }
                        }
                    }
                }
            ],
            'theme': {
                'name': 'material'
            }
        }

        return config_data

    def create_mkdocs_config_if_not_exists(self, comp):

        file = (self.base_path / f'{comp.name}/mkdocs.yaml')

        if file.exists():
            return

        with (self.base_path / f'{comp.name}/mkdocs.yaml').open('w') as f:
            yaml.dump(self.default_config(comp), f, default_flow_style=False)

    def create_docs(self, comp: CatDocsComponent):
        path = self.base_path / comp.name
        python_files = list(path.glob('**/*.py'))

        logger.debug(f'Creating docs folder in path {path}')
        docs_folder = path / f'docs'
        docs_folder.mkdir(exist_ok=True)
        logger.debug(f'Successfully created docs folder in path {docs_folder}')

        # Create default index

        if (docs_folder / 'index.md').exists():
            pass
        elif (path/ 'README.md').exists():
            shutil.copy((path/ 'README.md'), docs_folder / 'index.md')
        else:
            with (docs_folder / 'index.md').open('w') as f:
                f.write(f'# {comp.name}\n')
                f.write(f'Welcome to the automatically generated documentation for {comp.name}')



        for file in python_files:
            relative_path = str(file).split(comp.name)[1]
            relative_path = relative_path.strip('/')

            docs_path = (docs_folder / relative_path)
            docs_path.parent.mkdir(exist_ok=True, parents=True)

            if docs_path.name == '__init__.py':
                _f = (docs_path.parent.parent / 'index.md')
                _f.touch(exist_ok=True)
            else:
                _f = docs_path.with_suffix('.md')
                _f.touch(exist_ok=True)

            members = extract_names_in_order(file)
            module_path = str(Path(relative_path).with_suffix('')).replace('/', '.')
            if not members:
                continue

            with _f.open('w') as f:
                f.write(f':::{module_path}\n\n')

                for members in members:
                    name = members[1]
                    f.write(f':::{module_path}.{name}\n\n')

        pass

    def build(self, comp: CatDocsComponent):
        """
           Run MkDocs on a given folder.

           Args:
               folder_path (str): The path to the folder containing MkDocs configuration file (mkdocs.yml).
           """
        try:
            folder_path = self.base_path / comp.name

            # Check if mkdocs.yml exists in the folder
            if not (folder_path / "mkdocs.yaml").is_file():
                logger.error(f"Error: mkdocs.yml not found in {folder_path}.")
                return

            # Change directory to the folder path
            os.chdir(folder_path)
            # Run MkDocs build command
            logger.info(f'Building documentation for component {comp.name}')
            output = subprocess.run(["python", "-m", "mkdocs", "build"])
            if output.returncode == 0:
                logger.info("MkDocs build completed successfully.")
            else:
                raise Exception(f'Failed to generate documentation for {comp}.')
        except Exception as e:
            logger.exception(f"Failed to run MkDocs on folder: {folder_path}. Error: {e}")
            raise

    @staticmethod
    def move_docs(comp: CatDocsComponent):
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


def extract_names_in_order(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the content as an Abstract Syntax Tree (AST)
    tree = ast.parse(content, filename=file_path)

    names_in_order = []

    # Visit each node in the AST
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            names_in_order.append(('function', node.name))
        elif isinstance(node, ast.ClassDef):
            names_in_order.append(('class', node.name))

    return names_in_order
