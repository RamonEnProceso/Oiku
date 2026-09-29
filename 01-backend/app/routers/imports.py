from fastapi import APIRouter, Depends, HTTPException, UploadFile
from app.services.csv.read import readFile
from app.services.csv.csvIntoSQL import csvIntoSQLES
from sqlalchemy.orm import Session
from app.db.dependencies import get_db

router = APIRouter(
    prefix="/import",
    tags=["Import"]
)

@router.post("/csv/es/")
def import_csv_es_route(file:UploadFile, db:Session = Depends(get_db)):
    if file.content_type != "text/csv":
        raise HTTPException(
                    status_code=406,
                    detail="File is not a CSV")
    
    return csvIntoSQLES(file, db)