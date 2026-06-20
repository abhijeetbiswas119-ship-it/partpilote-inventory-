


from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.db.base import Base


# Types of stock movement
class TransactionType(str, enum.Enum):
    IN = "IN"
    OUT = "OUT"
    ADJUSTMENT = "ADJUSTMENT"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)

    # Which item changed stock
    item_id = Column(Integer, ForeignKey("inventory_items.id"), nullable=False)

    # Who did the action (user system later)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    transaction_type = Column(Enum(TransactionType), nullable=False)

    quantity = Column(Integer, nullable=False)

    # optional pricing (future analytics)
    unit_price = Column(Float, nullable=True)

    # optional reference (PO, repair job, etc.)
    reference = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # relationships
    item = relationship("InventoryItem", back_populates="transactions")
    user = relationship("User", back_populates="transactions")