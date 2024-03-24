from messaging_tools import Message

from core_api.core.reader import repo_reader
from core_api.event.events import Events
from core_api.event.message_broker import produce_message

async def on_start_up():

    components = repo_reader.files()
    for component in components:
        event = Message(
            type=Events.COMPONENT_CREATED,
            body=component
        )

        await produce_message(event)