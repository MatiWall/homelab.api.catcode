from fastapi import APIRouter, Response
from fastapi.exceptions import HTTPException
import settings

router = APIRouter(prefix='/docs')

# @router.get('/static/{system}/{application}/{deployableUnit}')
# def return_static_css(system, application, deployableUnit):
#
#     file_path = settings.BASE_DIR / f'builds/{system}.{application}.{deployableUnit}/site/assets/stylesheets'
#     pattern = 'main.*.min.css'
#     # Use glob to find matching files
#     matching_files = list(file_path.glob(pattern))[0]
#     try:
#         with matching_files.open('r') as file:
#             html_content = file.read()
#
#         return Response(content=html_content, media_type="text/css")
#     except FileNotFoundError:
#         return {"message": "Documentation file not found"}


@router.get('/static/{system}/{application}/{deployableUnit}')
def return_static_css(system: str, application: str, deployableUnit: str):
    # Construct the base path to the directory containing the CSS files
    base_path = settings.BASE_DIR / f'builds/{system}.{application}.{deployableUnit}/site/assets/stylesheets'

    # Define the pattern to match the desired CSS file
    pattern = 'main.*.min.css'

    # Use glob to find matching files
    matching_files = list(base_path.glob(pattern))

    # Check if any matching files were found
    if not matching_files:
        raise HTTPException(status_code=404, detail=f"CSS file not found for {base_path}")
    elif len(matching_files) > 1:
        raise HTTPException(status_code=500, detail=f"Found multiple CSS files for {base_path}")

    # Select the first matching file (you could enhance this to choose the most appropriate file if needed)
    css_file_path = matching_files[0]

    try:
        # Open the file and read its contents
        with css_file_path.open('r') as file:
            css_content = file.read()

        # Return the CSS content with the appropriate media type
        return Response(content=css_content, media_type="text/css")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="CSS file not found")
    except IOError:
        raise HTTPException(status_code=500, detail="Error reading the CSS file")
@router.get('/{system}/{application}/{deployableUnit}/{path:path}')
def return_html_docs(system, application, deployableUnit, path):
    print(system, application, deployableUnit, path)
    file_path = settings.BASE_DIR / f'builds/{system}.{application}.{deployableUnit}/site/{path}/index.html'
    try:
        with file_path.open('r') as file:
            html_content = file.read()

        return Response(content=html_content, media_type="text/html")
    except FileNotFoundError:
        return {"message": "Documentation file not found"}

