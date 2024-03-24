from messaging_tools import Message
from core_api.event.event_bus import event_bus
from core_api.event.handlers import on_start_up
from core_api.event.message_broker import consume_message
from core_api.event.events import Events


async def service():
    await on_start_up()


    await consume_message(event_bus)