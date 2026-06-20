

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse
)

from app.services.category_service import (
    get_all_categories,
    get_category_by_id,
    create_category,
    update_category,
    delete_category
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


# GET ALL CATEGORIES
@router.get("/", response_model=list[CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    return get_all_categories(db)


# GET ONE CATEGORY
@router.get("/{category_id}", response_model=CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = get_category_by_id(db, category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


# CREATE CATEGORY
@router.post("/", response_model=CategoryResponse)
def add_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return create_category(db, category)


# UPDATE CATEGORY
@router.put("/{category_id}", response_model=CategoryResponse)
def edit_category(
    category_id: int,
    updated_category: CategoryUpdate,
    db: Session = Depends(get_db)
):
    category = update_category(
        db,
        category_id,
        updated_category
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


# DELETE CATEGORY
@router.delete("/{category_id}")
def remove_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = delete_category(db, category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {
        "message": "Category deleted successfully"
    }