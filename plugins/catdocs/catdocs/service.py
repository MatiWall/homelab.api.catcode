import asyncio

from catdocs.read_componnets import read_components


async def service():
    components = await read_components()
    while True:

        await asyncio.sleep(10)

