import asyncio

from scheduler.queue import queue

async def event_emitter():
    while True:
        event = await queue.get()
        print(event)
        if queue.empty():
            await asyncio.sleep(0.5)