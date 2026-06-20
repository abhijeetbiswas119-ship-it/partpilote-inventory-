

from app.db.base import Base
from app.db.database import engine

from app.models.user import User
from app.models.inventory import InventoryItem
from app.models.category import Category
from app.models.transaction import Transaction


def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Supabase tables created successfully")