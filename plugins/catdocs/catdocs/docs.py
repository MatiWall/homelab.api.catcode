import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

router = APIRouter(prefix='/docs')

def validate_site_exists(site_name: str):
    # Check if the requested MkDocs site exists
    site_path = f"docs/{site_name}"
    return os.path.exists(site_path) and os.path.isdir(site_path)

@router.get("/{site_name}", response_class=HTMLResponse)
@router.get("/{site_name}/{filename:path}", response_class=HTMLResponse)
def get_docs(site_name: str, filename: str = "index.html"):
    if not validate_site_exists(site_name):
        raise HTTPException(status_code=404, detail="Documentation not found")

    # Serve MkDocs index.html or other HTML pages for the requested site
    return FileResponse(f"docs/{site_name}/{filename}")

# Mount the static files (CSS, JS, etc.) from the MkDocs site
router.mount("/extensions-opentelemetry", StaticFiles(directory=os.path.join("docs", "extensions-opentelemetry"), html=True), name="static")

