from catdocs.tools import mkdocs_handler

async def build_docs(event):
    mkdocs_handler.build(event.body)
