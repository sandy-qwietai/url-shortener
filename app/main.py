from fastapi import FastAPI
from app.routers.url_shortener import router as url_shortener_router

app = FastAPI()

app.include_router(url_shortener_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)