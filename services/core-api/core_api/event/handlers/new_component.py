import logging

from core_api.core.reader.models import CatCodeRepoEntry
from core_api.event.message_broker import produce_message

logger = logging.getLogger(__name__)
from messaging_tools import Message

from core_api.core.componentcache import cache, tracked_paths
from core_api.event.events import Events
async def new_component(event):
    repo = CatCodeRepoEntry(**event.body)
    logger.debug(f'Updating cache with {repo}')
    status = tracked_paths.add(repo)
    if status in ('Updated', 'New'):
        event = Message(
            type=Events.COMPONENT_UPDATED,
            body=repo
        )

        await produce_message(event)