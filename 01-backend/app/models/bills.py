from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy import func
from decimal import Decimal
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .subcategory import Subcategory
    from .account import Account

class Bills(Base):
    __tablename__="bills"
    id: Mapped[int] = mapped_column(primary_key=True)
    subcategory_id : Mapped[int] = mapped_column(ForeignKey("bills_subcategory.id"), nullable=False)
    account_id : Mapped[int] = mapped_column(ForeignKey("bills_account.id"), nullable=False)
    amount : Mapped[Decimal] = mapped_column(Numeric(12,2), nullable=False)
    description : Mapped[str] = mapped_column(String)
    ocurred_at : Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    created_at : Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at : Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    
    subcategory : Mapped ["Subcategory"] = relationship("Subcategory", back_populates="bills")
    account : Mapped ["Account"] = relationship("Account", back_populates="bills")
    
    def __repr__(self):
        return f"Bills(id={self.id}, subcategory='{self.subcategory.name}', amount={self.amount})"