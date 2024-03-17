from event_tools import Event

from core_api.core.readers.github import GithubReader
from core_api.event.events import Events
from core_api.event.queue import queue

from settings import config

async def on_start_up(event):
    reader = GithubReader(username=config.username, token=config.github_token)

    components = reader.get_files()
    for component in components:
        event = Event(
            type=Events.NEW_COMPONENT,
            body=component
        )
        print(event)
        await queue.put(event)