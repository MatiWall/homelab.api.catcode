from extensions.configuration import read_configs_to_dataclass, hosting_environment
from extensions.opentelemetry.config import configure_logging

configure_logging(enable_otel=hosting_environment.is_production())

config = read_configs_to_dataclass()



