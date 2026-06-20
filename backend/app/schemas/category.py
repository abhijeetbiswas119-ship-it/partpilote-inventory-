

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Base schema
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


# Create schema
class CategoryCreate(CategoryBase):
    pass


# Update schema
class CategoryUpdate(CategoryBase):
    pass


# Response schema
class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True