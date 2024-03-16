import asyncio
import time

from scheduler.scheduler import scheduler
from scheduler.emitter import event_emitter

async def start_scheduler():
    scheduler.start()

async def start_emitter():
    await event_emitter()

async def main():
    # Start scheduler and emitter concurrently
    scheduler_task = asyncio.create_task(start_scheduler())
    emitter_task = asyncio.create_task(start_emitter())

    # Wait for both tasks to finish
    await asyncio.gather(scheduler_task, emitter_task)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()