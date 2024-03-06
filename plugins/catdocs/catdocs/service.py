import asyncio

from catdocs.read_componnets import read_components
from catdocs.reader import GitHubReader

from settings import BASe_DIR

async def service():
    components = await read_components()

    reader = GitHubReader()

    for comp in components:
        reader.read(comp, BASe_DIR / 'tmp')

    while True:

        await asyncio.sleep(10)

