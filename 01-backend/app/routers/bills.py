from fastapi import APIRouter, Depends
from app.db.dependencies import get_db
from app.schemas.bills import BillResponse
from sqlalchemy.orm import Session
from app.crud.bills import get_bills

router = APIRouter(
    prefix="/bills",
    tags=["Bills"]
)

@router.get("/",response_model=list[BillResponse])
def get_bills_route(db:Session = Depends(get_db)):
    return get_bills(db)