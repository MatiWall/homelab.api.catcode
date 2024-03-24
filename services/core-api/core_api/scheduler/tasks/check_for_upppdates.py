import logging
import asyncio

from core_api.event.handlers import check_for_updates

logger = logging.getLogger(__name__)


async def emit_check_for_updates():
    logger.debug('Checking for updates to tracked repos.')
    await check_for_updates()


