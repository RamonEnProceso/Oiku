from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.account import create_account, update_account, delete_account, get_account, get_accounts
from app.schemas.account import AccountCreate, AccountUpdate, AccountResponse

router = APIRouter(
    prefix="/account",
    tags=["Accounts"]
)

@router.get("/",response_model=list[AccountResponse])
def get_accounts_route(db:Session = Depends(get_db)):
    return get_accounts(db)

@router.get("/{account_id}", response_model=AccountResponse)
def get_account_route(account_id:int, db:Session = Depends(get_db)):
    account = get_account(db, account_id)
    
    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not founded"
        )
    
    return account

@router.post("/", response_model=AccountResponse)
def create_account_route(account:AccountCreate, db:Session = Depends(get_db)):
    return create_account(db, account)

@router.put("/{account_id}", response_model=AccountResponse)
def update_account_route(account:AccountUpdate, account_id:int, db:Session = Depends(get_db)):
    account = update_account(db, account_id, account)
    
    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not founded"
        )
        
    return account

@router.delete("/{account_id}")
def delete_account_route(account_id:int, db:Session = Depends(get_db)):
    account = delete_account(db, account_id)
    
    if account is None:
            raise HTTPException(
                status_code=404,
                detail="Account not founded"
            )
        
    return {"message":f"Account n{account_id} was deleted succesfully"}
