import logging
logger = logging.getLogger(__name__)

from pathlib import Path
from catdocs.tools import mkdocs_handler
from event_tools import Event
from catdocs.events import EventType
from catdocs.queue import event_queue
import settings
async def build_docs(event):
    mkdocs_handler.build(event.body)

    event = Event(
        type=EventType.MOVE_DOCS,
        body={
            'name': event.body.name
        }
    )
    await event_queue.put(event)


async def move_docs(event):
    initial_path = settings.BASE_DIR / f'tmp/{event.body["name"]}/site'
    final_path = settings.BASE_DIR / f'builds/{event.body["name"]}/site'

    logger.debug(f'Moving {event.body["name"]} from {initial_path} to {final_path}')

    # Create the build directory if it doesn't exist
    final_path.parent.mkdir(parents=True, exist_ok=True)

    # Move the file
    try:
        path = Path(initial_path)
        path.rename(final_path)
        logger.debug(f'Successfully moved {event.body["name"]} from {initial_path} to {final_path}')
    except Exception as e:
        logger.exception(f'Failed to move {event.body["name"]} from {initial_path} to {final_path}: {e}')