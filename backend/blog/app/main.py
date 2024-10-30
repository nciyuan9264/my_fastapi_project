from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from blog.app.core.config import settings
from blog.app.api.api import api_router

app = FastAPI()
print(type(settings.BACKEND_CORS_ORIGINS), settings.BACKEND_CORS_ORIGINS)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost:5173', 'http://localhost:8080'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)
