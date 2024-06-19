from pathlib import Path

from extensions.configuration import read_configs_to_dataclass, hosting_environment
from extensions.opentelemetry import configure_logging


BASE_DIR = Path(__file__).resolve().parent


configure_logging(
    enable_otel=hosting_environment.is_production(),
    level=10
)

config = read_configs_to_dataclass(BASE_DIR)



