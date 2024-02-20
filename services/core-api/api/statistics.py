
from fastapi import APIRouter
from .appplications import database


router = APIRouter(prefix='/statistics')

@router.get('/')
def get_applications():
    config = database.stats()

    return config