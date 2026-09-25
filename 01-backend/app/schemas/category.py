from pydantic import BaseModel, ConfigDict

class CategoryCreate(BaseModel):
    name: str
    
class CategoryUpdate(BaseModel):
    name: str | None = None
    
class CategoryResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    name: str