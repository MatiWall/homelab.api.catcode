from pathlib import Path
from subprocess import run as subprocess_run

class DocsBuilder:

    def __init__(
            self,
    ):
        pass

    def run(
            self,
            input_dir: Path,
            output_dir: Path
    ):
        subprocess_run(['mkdocs', 'build', '-d', output_dir, '-v'], cwd=input_dir)

