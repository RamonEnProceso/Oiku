from app.crud.bills import create_bill
from app.schemas.bills import BillCreate
from sqlalchemy.orm import Session

def create_bills_from_list(db: Session, bills: list[BillCreate]):
    for bill in bills:
        create_bill(db, bill)
    return True