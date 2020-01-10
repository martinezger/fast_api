from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def list_user():
    return dict(message="hello v2")
