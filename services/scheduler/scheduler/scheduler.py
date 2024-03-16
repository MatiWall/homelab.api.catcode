from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler.tasks import (
 emit_check_for_updates_event
)

scheduler = AsyncIOScheduler()

scheduler.add_job(emit_check_for_updates_event, 'interval', seconds=3)