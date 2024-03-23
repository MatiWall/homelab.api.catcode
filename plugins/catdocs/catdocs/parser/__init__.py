from catdocs.models import CatDocsComponent
from settings import config


def create_component_from_object(comp):
    return CatDocsComponent(
        url=comp['metadata'].get('annotations', {}).get(config.catcode_url_annotation),
        docs_path=comp['metadata'].get('annotations', {}).get(config.catdocs_path_annotation),
        repo_path=comp['metadata'].get('annotations', {}).get(config.catcode_repo_path_annotation),
        deployable_unit=comp['metadata']['deployableUnit'],
        application=comp['metadata']['application'],
        system=comp['metadata']['system']
    )
