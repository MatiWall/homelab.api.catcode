from catdocs.queue import event_queue
from catdocs.models import CatDocsComponent
from catdocs.cache import cache

async def on_component_created_or_changed(event):

    body  = event.body

    comp = create_component_from_object(body)
    # Update cache
    logger.debug('Updating cache on startup')
    cache.add(comp)
    logger.debug('Finished updating cache on startup')

    logger.info('Clone or update repositories')
    repo_handler.update_or_clone(comp)
    logger.info('Finished cloning or update repositories')

    await event_queue.put(
            Event(
                type=EventType.BUILD_DOCS,
                body=comp
            )
     )

