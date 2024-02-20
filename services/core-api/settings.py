from pathlib import Path
from extensions.configuration import read_configs_to_dataclass

BASE_DIR = Path(__file__).parent


config = read_configs_to_dataclass(BASE_DIR)