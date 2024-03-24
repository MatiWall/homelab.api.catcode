import logging

from catdocs.core.events import EventType
from catdocs.core.events.handlers import on_component_created_or_changed

logger = logging.getLogger(__name__)

from catdocs.read_componnets import read_components
async def on_startup():

    components = await read_components()

    for component in components:
        await on_component_created_or_changed(component)


