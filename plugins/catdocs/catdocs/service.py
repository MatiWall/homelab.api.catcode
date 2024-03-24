from catdocs.core.events import event_bus
from catdocs.core.events.handlers import on_startup
from catdocs.core.events.event_bus import event_bus

from catdocs.core.events.message_broker import consume_message


async def service():

    await on_startup()

    await consume_message(event_bus)

