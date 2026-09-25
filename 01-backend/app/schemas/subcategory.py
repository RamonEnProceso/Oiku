from pydantic import BaseModel, ConfigDict

class SubcategoryCreate(BaseModel):
    name: str
    category_id : int
    mindless_spending : bool
    
class SubcategoryUpdate(BaseModel):
    name: str | None = None
    category_id : int | None = None
    mindless_spending : bool | None = None
    
class SubcategorResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
    name: str
    category_id : int
    mindless_spending : bool