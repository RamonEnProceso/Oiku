from fastapi import APIRouter, Depends, HTTPException
from app.db.dependencies import get_db
from app.schemas.bills import BillResponse, BillCreate, BillUpdate
from app.schemas.subcategory import SubcategoryResponse
from app.schemas.account import AccountResponse
from sqlalchemy.orm import Session
from app.crud.bills import get_bills, get_bill, create_bill, update_bill, delete_bill, get_bill_account, get_bill_subcategory, delete_all_bills, get_bills_month, get_bills_year

router = APIRouter(
    prefix="/bills",
    tags=["Bills"]
)

@router.get("/",response_model=list[BillResponse])
def get_bills_route(db:Session = Depends(get_db)):
    return get_bills(db)

@router.get("/{year}/{month}",response_model=list[BillResponse])
def get_bills_by_month_route(year:int, month:int, db:Session = Depends(get_db)):
    return get_bills_month(db, year, month)

@router.get("/{year}/",response_model=list[BillResponse])
def get_bills_by_year(year:int, db:Session = Depends(get_db)):
    return get_bills_year(db, year)

@router.get("/{bill_id}", response_model=BillResponse)
def get_bill_route(bill_id:int, db:Session = Depends(get_db)):
    bill = get_bill(db, bill_id)
    
    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not founded"
        )
    
    return bill

@router.post("/", response_model=BillResponse)
def create_bill_route(bill:BillCreate, db:Session = Depends(get_db)):
    return create_bill(db, bill)

@router.put("/{bill_id}", response_model=BillResponse)
def update_bill_route(bill:BillUpdate, bill_id:int, db:Session = Depends(get_db)):
    bill = update_bill(db, bill_id, bill)
    
    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not founded"
        )
        
    return bill

@router.delete("/{bill_id}")
def delete_bill_route(bill_id:int, db:Session = Depends(get_db)):
    bill = delete_bill(db, bill_id)
    
    if bill is None:
            raise HTTPException(
                status_code=404,
                detail="Bill not founded"
            )
        
    return {"message":f"Bill n{bill_id} was deleted succesfully"}

@router.delete("/all/")
def delete_all_bills_route(db:Session = Depends(get_db)):
    delete_all_bills(db)
    
    return {"message":"Bills were deleted succesfully"}

@router.get("/{bill_id}/subcategory", response_model=SubcategoryResponse)
def get_bill_subcategory_route(bill_id:int, db:Session = Depends(get_db)):
    bill = get_bill(db, bill_id)
    
    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not founded"
        )
        
    return get_bill_subcategory(db, bill_id)
        
        
@router.get("/{bill_id}/account", response_model=AccountResponse)
def get_bill_account_route(bill_id:int, db:Session = Depends(get_db)):
    bill = get_bill(db, bill_id)
    
    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not founded"
        )
        
    return get_bill_account(db, bill_id)