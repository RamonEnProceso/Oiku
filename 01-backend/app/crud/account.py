from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Account
from app.schemas.account import AccountCreate, AccountUpdate

def create_account(db: Session, account: AccountCreate):
    accountDB = Account(
        name = account.name
    )
    db.add(accountDB)
    db.commit()
    db.refresh(accountDB)
    return accountDB

def get_accounts(db:Session):
    stmt = select(Account)
    return db.execute(stmt).scalars().all()

def get_account(db:Session, account_id: int):
    return db.get(Account, account_id)

def update_account(db:Session, account_id: int, account: AccountUpdate):
    accountDB = db.get(account, account_id)
    if accountDB is None:
        return None

    updated_data = Account.model_dump(exclude_unset=True)
   
    for key, value in updated_data.items():
        setattr(accountDB, key, value)

    db.commit()
    db.refresh(accountDB)
    return accountDB
        
def delete_account (db: Session, account_id:int):
    account = db.get(account, account_id)
    if account is None:
        return None
    
    db.delete(account)
    db.commit()
    return True