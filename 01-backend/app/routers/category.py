from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.category import create_category, update_category, delete_category, get_category, get_categories, get_category_subcategories, get_category_bills
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.schemas.subcategory import SubcategoryResponse
from app.schemas.bills import BillResponse

router = APIRouter(
    prefix="/category",
    tags=["Categories"]
)

@router.get("/",response_model=list[CategoryResponse])
def get_categories_route(db:Session = Depends(get_db)):
    return get_categories(db)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category_route(category_id:int, db:Session = Depends(get_db)):
    category = get_category(db, category_id)
    
    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not founded"
        )
    
    return category

@router.post("/", response_model=CategoryResponse)
def create_category_route(category:CategoryCreate, db:Session = Depends(get_db)):
    return create_category(db, category)

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category_route(category:CategoryUpdate, category_id:int, db:Session = Depends(get_db)):
    category = update_category(db, category_id, category)
    
    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not founded"
        )
        
    return category

@router.delete("/{category_id}")
def delete_category_route(category_id:int, db:Session = Depends(get_db)):
    category = delete_category(db, category_id)
    
    if category is None:
            raise HTTPException(
                status_code=404,
                detail="Category not founded"
            )
        
    return {"message":f"Category n{category_id} was deleted succesfully"}

@router.get("/{category_id}/subcategories", response_model=list[SubcategoryResponse])
def get_category_subcategories_route(category_id:int, db:Session = Depends(get_db)):
    category = get_category(db, category_id)
    
    if category is None:
            raise HTTPException(
                status_code=404,
                detail="Category not founded"
            )
        
    return get_category_subcategories(db, category_id)

@router.get("/{category_id}/bills", response_model=list[BillResponse])
def get_category_bills_route(category_id:int, db:Session = Depends(get_db)):
    category = get_category(db, category_id)
    
    if category is None:
            raise HTTPException(
                status_code=404,
                detail="Category not founded"
            )
        
    return get_category_bills(db, category_id)