from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Bills
from app.schemas.bills import BillCreate, BillUpdate

def create_bill(db: Session, bill: BillCreate):
    billDB = Bills(
        subcategory_id = bill.subcategory,
        account_id = bill.account,
        amount = bill.amount,
        description = bill.description,
        ocurred_at = bill.ocurred_at,
        created_at = bill.created_at,
        updated_at = bill.updated_at
    )
    db.add(billDB)
    db.commit()
    db.refresh(billDB)
    return billDB

def get_bills(db:Session):
    stmt = select(Bills)
    return db.execute(stmt).scalars().all()

def get_bill(db:Session, bill_id: int):
    return db.get(Bills, bill_id)

def update_cliente(db:Session, bill: BillUpdate, bill_id: int):
    billDB = db.get(Bills, bill_id)
    if billDB is None:
        return None
    
    updated_data = bill.model_dump(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(billDB, key, value)
        
def delete_bill (db: Session, bill_id:int):
    bill = db.get(Bills, bill_id)
    if bill is None:
        return None
    
    db.delete(bill)
    db.commit()
    return True

def get_bill_subcategory(db:Session, bill_id:int):
    bill = db.get(Bills, bill_id)
    if bill is None:
        return None
    
    return bill.subcategory

def get_bill_account(db:Session, bill_id:int):
    bill = db.get(Bills, bill_id)
    if bill is None:
        return None
    
    return bill.account