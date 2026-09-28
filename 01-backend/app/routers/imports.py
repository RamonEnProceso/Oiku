from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.db.dependencies import get_db

router = APIRouter(
    prefix="/import",
    tags=["Import"]
)

@router.post("/csv/")
def import_csv_route(file:UploadFile):
    if file.content_type != "text/csv":
        raise HTTPException(
                    status_code=406,
                    detail="File is not a CSV"
                )
    
    return {"type":file.content_type}