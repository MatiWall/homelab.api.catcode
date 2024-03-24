from extensions.rabbitmq import AsyncRabbitMQProducer, AsyncRabbitMQConsumer
from messaging_tools import EventBus, Message

from settings import config

async def produce_message(message):

    async with AsyncRabbitMQProducer(url=config.rabbitmq_url) as producer:
        await producer.publish('events', message.model_dump_json())


async def consume_message(bus: EventBus):

    async def callback(message):
        msg = Message.model_validate_json(message)
        await bus.emit(msg)

    async with AsyncRabbitMQConsumer(config.rabbitmq_url) as consumer:
        await consumer.consume('events', callback=callback)