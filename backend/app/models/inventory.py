

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True)

    part_number = Column(String, unique=True, index=True, nullable=False)
    manufacturer_part_number = Column(String, nullable=True)

    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    category_id = Column(Integer, ForeignKey("categories.id"))

    quantity_in_stock = Column(Integer, default=0)
    minimum_stock_level = Column(Integer, default=10)

    unit_price = Column(Float, nullable=True)

    package_type = Column(String, nullable=True)
    value = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    category = relationship("Category", back_populates="items")
    
    transactions = relationship("Transaction", back_populates="item")