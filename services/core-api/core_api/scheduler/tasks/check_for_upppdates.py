import logging
logger = logging.getLogger(__name__)

from messaging_tools import Message
from core_api.event.events import Commands
from core_api.event.queue import queue

def emit_check_for_updates_event():
    logger.debug('Checking for updates to tracked repos.')
    event = Message(
        type=Commands.LOOK_FOR_CHANGES
    )
    queue.put_nowait(event)


