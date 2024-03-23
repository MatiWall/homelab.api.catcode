import logging
logger = logging.getLogger(__name__)

from core_api.core.componentcache import cache, tracked_paths
from core_api.event.events import Events
from core_api.core.reader import repo_reader
async def check_for_updates(event):
    files = repo_reader.get_files()
    for file in files:
        resp = tracked_paths.add(file)

        if resp in ('New', 'Updated'):
            event = Event(
                type=Events.UPDATED_COMPONENT,
                body=file
            )
            await queue.put(event)

    repos = set([file.name for file in files])
    cached_repos = set(tracked_paths.get_all().keys())
    deleted_repos = cached_repos - repos
    try:
        tracked_paths.remove(list(deleted_repos))
    except Exception as e:
        logger.exception(f'Failed to remove deleted components with error:\n')
        return

    for deleted_file in [file for file in files if file.name in deleted_repos]:
        event = Events(
            type=Events.DELETED_COMPONENT,
            body=deleted_file
        )
        await queue.put(event)



async def update_cache(event):
    logger.debug(f'Updating cache with component {event.body}')
    component = repo_reader.get_file_content(event.body)
    cache.add(component)


async def externally_publish(event):
    print('Submit to rabbitmq')
