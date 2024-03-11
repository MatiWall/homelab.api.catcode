from fastapi import APIRouter, Response
import settings

router = APIRouter(prefix='/docs')


@router.get('/{system}/{application}/{deployableUnit}')
def return_docs(system, application, deployableUnit):

    file_path = settings.BASE_DIR / f'builds/{system}.{application}.{deployableUnit}/site/index.html'
    try:
        with file_path.open('r') as file:
            html_content = file.read()

        return Response(content=html_content, media_type="text/html")
    except FileNotFoundError:
        return {"message": "Documentation file not found"}
