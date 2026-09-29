from pandas import DataFrame, isna
from app.schemas.bills import BillCreate
from app.services.csv.TypeToID import convertTypeToID
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

## Por ahora solo existe en español porque lo uso solo yo :p

def convertToDecimal (str:str):
    num = Decimal(str.replace(",", "")).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return abs(num)

def convertCSVToPydantic (df:DataFrame) :
    bills = []
    
    for index, row in df.iterrows():
        try:
            rowAmount = convertToDecimal(row["Monto"])
            rowType = row["Categoría"]
            rowDescription = "" if isna(row["Descripción"]) else row["Descripción"]
                    
            bill = BillCreate(
                occurred_at=datetime.strptime(row["Fecha"],'%d/%m/%Y'),
                description=rowDescription,
                subcategory=convertTypeToID(rowAmount,rowDescription,rowType),
                amount= rowAmount,
                account=1,
                created_at=datetime.now(),
                updated_at=datetime.now()
                )
            bills.append(bill)
        except:
            continue
    
    return bills