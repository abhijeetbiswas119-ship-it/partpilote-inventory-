

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.inventory import InventoryItem
from app.core.deps import get_current_user
from fastapi import Depends
from app.core.security import oauth2_scheme

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/")
def get_inventory(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    return db.query(InventoryItem).all()

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
    
@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {
        "message": "You are authenticated",
        "token": token
    }