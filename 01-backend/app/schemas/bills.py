from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import datetime

class BillCreate(BaseModel):
    name: str
    subcategory: int
    account: int
    amount: Decimal
    description: str | None = None
    ocurred_at: datetime
    created_at: datetime
    updated_at: datetime
    
class BillUpdate(BaseModel):
    name: str | None = None
    subcategory: int | None = None
    account: int | None = None
    amount: Decimal | None = None
    description: str | None = None
    ocurred_at: datetime | None = None
    updated_at: datetime
    
class BillResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
    name: str
    subcategory: int
    account: int
    amount: Decimal
    description: str | None = None
    ocurred_at: datetime
    created_at: datetime
    updated_at: datetime
    