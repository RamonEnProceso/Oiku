from pydantic import BaseModel, ConfigDict

class CategoryCreate(BaseModel):
    name: str
    
class CategoryUpdate(BaseModel):
    name: str | None = None
    
class CategorResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
    name: str