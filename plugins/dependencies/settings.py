from pathlib import Path
from extensions.configuration import read_configs_to_dataclass
from extensions.opentelemetry import configure_logging

BASE_DIR = Path(__file__).resolve().parent

config = read_configs_to_dataclass(path=BASE_DIR)