from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.subcategory import create_subcategory, update_subcategory, delete_subcategory, get_subcategory, get_subcategories, get_subcategory_bills, get_subcategory_category
from app.schemas.category import CategoryResponse
from app.schemas.subcategory import SubcategoryResponse, SubcategoryCreate, SubcategoryUpdate
from app.schemas.bills import BillResponse

router = APIRouter(
    prefix="/subcategory",
    tags=["Subcategories"]
)

@router.get("/",response_model=list[SubcategoryResponse])
def get_subcategories_route(db:Session = Depends(get_db)):
    return get_subcategories(db)

@router.get("/{subcategory_id}", response_model=SubcategoryResponse)
def get_subcategory_route(subcategory_id:int, db:Session = Depends(get_db)):
    subcategory = get_subcategory(db, subcategory_id)
    
    if subcategory is None:
        raise HTTPException(
            status_code=404,
            detail="Subcategory not founded"
        )
    
    return subcategory

@router.post("/", response_model=SubcategoryResponse)
def create_subcategory_route(subcategory:SubcategoryCreate, db:Session = Depends(get_db)):
    return create_subcategory(db, subcategory)

@router.put("/{subcategory_id}", response_model=SubcategoryResponse)
def update_subcategory_route(subcategory_data:SubcategoryUpdate, subcategory_id:int, db:Session = Depends(get_db)):
    subcategory = update_subcategory(db, subcategory_id, subcategory_data)
    
    if subcategory is None:
        raise HTTPException(
            status_code=404,
            detail="Subcategory not founded"
        )
        
    return subcategory

@router.delete("/{subcategory_id}")
def delete_subcategory_route(subcategory_id:int, db:Session = Depends(get_db)):
    subcategory = delete_subcategory(db, subcategory_id)
    
    if subcategory is None:
            raise HTTPException(
                status_code=404,
                detail="Subcategory not founded"
            )
        
    return {"message":f"Subcategory n{subcategory_id} was deleted succesfully"}

@router.get("/{category_id}/subcategories", response_model=CategoryResponse)
def get_subcategory_category_route(subcategory_id:int, db:Session = Depends(get_db)):
    subcategory = get_subcategory(db, subcategory_id)
    
    if subcategory is None:
            raise HTTPException(
                status_code=404,
                detail="Subcategory not founded"
            )
        
    return get_subcategory_category(db, subcategory_id)

@router.get("/{subcategory_id}/bills", response_model=list[BillResponse])
def get_subcategory_bills_route(subcategory_id:int, db:Session = Depends(get_db)):
    subcategory = get_subcategory(db, subcategory_id)
    
    if subcategory is None:
            raise HTTPException(
                status_code=404,
                detail="Subcategory not founded"
            )
        
    return get_subcategory_bills(db, subcategory_id)