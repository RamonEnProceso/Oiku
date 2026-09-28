from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Subcategory
from app.schemas.subcategory import SubcategoryCreate, SubcategoryUpdate

def create_subcategory(db: Session,subcategory: SubcategoryCreate):
    subcategoryDB = Subcategory(
        name =subcategory.name
    )
    db.add(subcategoryDB)
    db.commit()
    db.refresh(subcategoryDB)
    return subcategoryDB

def get_subcategories(db:Session):
    stmt = select(Subcategory)
    return db.execute(stmt).scalars().all()

def get_subcategory(db:Session,subcategory_id: int):
    return db.get(Subcategory,subcategory_id)

def update_subcategory(db:Session,subcategory_id: int,subcategory: SubcategoryUpdate):
    subcategoryDB = db.get(Subcategory,subcategory_id)
    if subcategoryDB is None:
        return None

    updated_data =subcategory.model_dump(exclude_unset=True)
   
    for key, value in updated_data.items():
        setattr(subcategoryDB, key, value)

    db.commit()
    db.refresh(subcategoryDB)
    return subcategoryDB
        
def delete_subcategory (db: Session,subcategory_id:int):
    subcategory = db.get(Subcategory,subcategory_id)
    if subcategory is None:
        return None
    
    db.delete(subcategory)
    db.commit()
    return True

def get_subcategory_category (db: Session,subcategory_id:int):
    subcategory = db.get(Subcategory,subcategory_id)
    if subcategory is None:
        return None
    
    return subcategory.category

def get_subcategory_bills (db: Session,subcategory_id:int):
    subcategory = db.get(Subcategory,subcategory_id)
    if subcategory is None:
        return None
    
    return subcategory.bills