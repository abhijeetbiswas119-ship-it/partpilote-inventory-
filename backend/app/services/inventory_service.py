
from sqlalchemy.orm import Session

from app.models.inventory import InventoryItem
from app.schemas.inventory import InventoryCreate, InventoryUpdate


# Get all inventory items
def get_all_items(db: Session):
    return db.query(InventoryItem).all()


# Get one inventory item
def get_item_by_id(db: Session, item_id: int):
    return db.query(InventoryItem).filter(
        InventoryItem.id == item_id
    ).first()


# Create inventory item
def create_item(db: Session, item: InventoryCreate):
    db_item = InventoryItem(**item.model_dump())

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


# Update inventory item
def update_item(
    db: Session,
    item_id: int,
    updated_item: InventoryUpdate
):
    item = get_item_by_id(db, item_id)

    if not item:
        return None

    for key, value in updated_item.model_dump().items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)

    return item


# Delete inventory item
def delete_item(db: Session, item_id: int):
    item = get_item_by_id(db, item_id)

    if not item:
        return None

    db.delete(item)
    db.commit()

    return item