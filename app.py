import uvicorn
from fastapi import FastAPI

from api.v1 import api_router as api_v1
from api.v2 import api_router as api_v2
from config import DevConfig



def create_app(config=DevConfig):
    app = FastAPI(title=config.PROJECT_NAME, openapi_prefix="/api/v1/openapi.json")
    app.include_router(api_v1, prefix=config.API_V1_PREFIX)
    app.include_router(api_v2, prefix=config.API_V2_PREFIX)

    return app
