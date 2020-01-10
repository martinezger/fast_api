from fastapi.routing import APIRouter

from api.v2 import user

api_router = APIRouter()
api_router.include_router(user.router, prefix='/user')
