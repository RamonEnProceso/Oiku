from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

def create_category(db: Session, category: CategoryCreate):
    categoryDB = Category(
        name = category.name
    )
    db.add(categoryDB)
    db.commit()
    db.refresh(categoryDB)
    return categoryDB

def get_categories(db:Session):
    stmt = select(Category)
    return db.execute(stmt).scalars().all()

def get_category(db:Session, category_id: int):
    return db.get(Category, category_id)

def update_category(db:Session, category_id: int, category: CategoryUpdate):
    categoryDB = db.get(Category, category_id)
    if categoryDB is None:
        return None

    updated_data = category.model_dump(exclude_unset=True)
   
    for key, value in updated_data.items():
        setattr(categoryDB, key, value)

    db.commit()
    db.refresh(categoryDB)
    return categoryDB
        
def delete_category (db: Session, category_id:int):
    category = db.get(Category, category_id)
    if category is None:
        return None
    
    db.delete(category)
    db.commit()
    return True

def get_category_subcategories (db: Session, category_id:int):
    category = db.get(Category, category_id)
    if category is None:
        return None
    
    return category.subcategories

def get_category_bills (db: Session, category_id:int):
    category = db.get(Category, category_id)
    if category is None:
        return None
    
    subcategories = category.subcategories
    
    bills = []
    
    for subcategory in subcategories:
        bills.append(subcategory.bills)
    
    return bills
