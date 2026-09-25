from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bills import Bills

class Account(Base):
    __tablename__="bills_account"
    id: Mapped[int] = mapped_column(primary_key=True) 
    name : Mapped[str] = mapped_column(String)
    
    bills : Mapped[list["Bills"]] = relationship("Bills", back_populates="account")
    
    def __repr__(self):
        return f"Account(id={self.id}, name='{self.name}')"