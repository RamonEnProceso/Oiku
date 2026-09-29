from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from app.models import Bills
from app.schemas.bills import BillCreate, BillUpdate
from datetime import datetime

def create_bill(db: Session, bill: BillCreate):
    billDB = Bills(
        subcategory_id = bill.subcategory,
        account_id = bill.account,
        amount = bill.amount,
        description = bill.description,
        occurred_at = bill.occurred_at,
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

def get_bills_month(db:Session, year:int, month:int):
    start = datetime(year, month, 1)

    if month == 12:
        end = datetime(year + 1, 1, 1)
    else:
        end = datetime(year, month + 1, 1)

    stmt = select(Bills).where(
        Bills.occurred_at >= start,
        Bills.occurred_at < end
    )

    return db.execute(stmt).scalars().all()

def get_bills_year(db:Session, year:int):
    start = datetime(year, 1, 1)
    end = datetime(year + 1 , 1, 1)

    stmt = select(Bills).where(
        Bills.occurred_at >= start,
        Bills.occurred_at < end
    )

    return db.execute(stmt).scalars().all()

def get_bill(db:Session, bill_id: int):
    return db.get(Bills, bill_id)

def update_bill(db:Session, bill_id: int, bill: BillUpdate):
    billDB = db.get(Bills, bill_id)
    if billDB is None:
        return None

    updated_data = bill.model_dump(exclude_unset=True)
   
    if "subcategory" in updated_data:
        updated_data["subcategory_id"] = updated_data.pop("subcategory")
    if "account" in updated_data:
        updated_data["account_id"] = updated_data.pop("account")

    for key, value in updated_data.items():
        setattr(billDB, key, value)

    db.commit()
    db.refresh(billDB)
    return billDB
        
def delete_bill (db: Session, bill_id:int):
    bill = db.get(Bills, bill_id)
    if bill is None:
        return None
    
    db.delete(bill)
    db.commit()
    return True

def delete_all_bills (db: Session):
    stmt = delete(Bills)
    db.execute(stmt)
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