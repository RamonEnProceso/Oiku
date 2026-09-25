from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/bills",
    tags=["Bills"]
)

