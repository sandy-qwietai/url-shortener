from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from app.services.url_service import shorten_url, get_original_url, get_top_domains
from app.schemas.url_schema import URLRequest


router = APIRouter()


@router.post("/url/shorten")
async def get_short_url(request: URLRequest, req: Request):
    url = request.url
    if not url:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No URL provided")
    short_url = shorten_url(url)
    return {"short_url": str(req.base_url) + short_url}

@router.get("/{short_url}")
async def redirect_to_url(short_url: str):
    original_url = get_original_url(short_url)
    if original_url:
        return RedirectResponse(original_url)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")

@router.get("/url/metrics")
async def metrics():
    return get_top_domains()