from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .subcategory import Subcategory

class Category(Base):
    __tablename__="bills_category"
    id: Mapped[int] = mapped_column(primary_key=True) 
    name : Mapped[str] = mapped_column(String)
    
    subcategories : Mapped[list["Subcategory"]] = relationship("Subcategory", back_populates="bills_subcategory")
    
    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"