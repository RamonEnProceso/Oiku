from app.services.csv.read import read_csv
from app.services.csv.conversorES import convertCSVToPydantic as conversorES
from app.services.csv.pydanticListToSQL import create_bills_from_list
from app.schemas.bills import BillCreate
from sqlalchemy.orm import Session
from fastapi import UploadFile

def csvIntoSQLES(file:UploadFile, db:Session):
    df = read_csv(file.file)
    bills = conversorES(df)
    create_bills_from_list(db, bills)
    return bills