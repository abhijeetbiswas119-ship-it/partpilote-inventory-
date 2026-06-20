

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Base schema
class InventoryBase(BaseModel):
    part_number: str
    manufacturer_part_number: Optional[str] = None
    name: str
    description: Optional[str] = None

    category_id: Optional[int] = None

    quantity_in_stock: int = 0
    minimum_stock_level: int = 10

    unit_price: Optional[float] = None

    package_type: Optional[str] = None
    value: Optional[str] = None

    is_active: bool = True


# Create schema
class InventoryCreate(InventoryBase):
    pass


# Update schema
class InventoryUpdate(InventoryBase):
    pass


# Response schema
class InventoryResponse(InventoryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True