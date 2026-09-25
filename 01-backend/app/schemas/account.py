from pydantic import BaseModel, ConfigDict

class AccountCreate(BaseModel):
    name: str
    
class AccountUpdate(BaseModel):
    name: str | None = None
    
class AccountResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    name: str