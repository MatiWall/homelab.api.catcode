from messaging_tools import Message

from core_api.core.reader import repo_reader
from core_api.event.events import Events
from core_api.event.queue import queue

from settings import config

async def on_start_up(event):

    components = repo_reader.files()
    for component in components:
        event = Message(
            type=Events.NEW_COMPONENT,
            body=component
        )
        print(event)
        await queue.put(event)