from fastapi import APIRouter, Response
import settings

router = APIRouter(prefix='/docs')

@router.get('/static/{system}/{application}/{deployableUnit}')
def return_static_css(system, application, deployableUnit):

    file_path = settings.BASE_DIR / f'builds/{system}.{application}.{deployableUnit}/site/assets/stylesheets/main.7e359304.min.css'
    try:
        with file_path.open('r') as file:
            html_content = file.read()

        return Response(content=html_content, media_type="text/css")
    except FileNotFoundError:
        return {"message": "Documentation file not found"}
@router.get('/{system}/{application}/{deployableUnit}/{path:path}')
def return_html_docs(system, application, deployableUnit, path):

    file_path = settings.BASE_DIR / f'builds/{system}.{application}.{deployableUnit}/site/{path}/index.html'
    try:
        with file_path.open('r') as file:
            html_content = file.read()

        return Response(content=html_content, media_type="text/html")
    except FileNotFoundError:
        return {"message": "Documentation file not found"}

