from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean
from sqlalchemy import String

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .category import Category
    from .bills import Bills

class Subcategory(Base):
    __tablename__="bills_subcategory"
    id: Mapped[int] = mapped_column(primary_key=True)
    category_id : Mapped[int] = mapped_column(ForeignKey("bills_category.id"), nullable=False)
    name : Mapped[str] = mapped_column(String)
    mindless_spending : Mapped[bool] = mapped_column(Boolean)
    
    category : Mapped ["Category"] = relationship("Category", back_populates="subcategories")
    bills : Mapped[list["Bills"]] = relationship("Bills", back_populates="subcategory")
    
    def __repr__(self):
        return f"Subcategory(id={self.id}, name='{self.name}', category={self.category.name})"