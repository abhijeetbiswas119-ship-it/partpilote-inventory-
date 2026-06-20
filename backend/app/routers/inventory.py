

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.inventory import (
    InventoryCreate,
    InventoryUpdate,
    InventoryResponse
)

from app.services.inventory_service import (
    get_all_items,
    get_item_by_id,
    create_item,
    update_item,
    delete_item
)

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


# GET ALL ITEMS
@router.get("/", response_model=list[InventoryResponse])
def read_inventory(db: Session = Depends(get_db)):
    return get_all_items(db)


# GET ONE ITEM
@router.get("/{item_id}", response_model=InventoryResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item_by_id(db, item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


# CREATE ITEM
@router.post("/", response_model=InventoryResponse)
def add_item(
    item: InventoryCreate,
    db: Session = Depends(get_db)
):
    return create_item(db, item)


# UPDATE ITEM
@router.put("/{item_id}", response_model=InventoryResponse)
def edit_item(
    item_id: int,
    updated_item: InventoryUpdate,
    db: Session = Depends(get_db)
):
    item = update_item(
        db,
        item_id,
        updated_item
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


# DELETE ITEM
@router.delete("/{item_id}")
def remove_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = delete_item(db, item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return {
        "message": "Item deleted successfully"
    }