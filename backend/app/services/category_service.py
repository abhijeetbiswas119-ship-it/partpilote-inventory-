


from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


# Get all categories
def get_all_categories(db: Session):
    return db.query(Category).all()


# Get category by ID
def get_category_by_id(db: Session, category_id: int):
    return (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )


# Create category
def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.model_dump())

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


# Update category
def update_category(
    db: Session,
    category_id: int,
    updated_category: CategoryUpdate
):
    category = get_category_by_id(db, category_id)

    if not category:
        return None

    for key, value in updated_category.model_dump().items():
        setattr(category, key, value)

    db.commit()
    db.refresh(category)

    return category


# Delete category
def delete_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)

    if not category:
        return None

    db.delete(category)
    db.commit()

    return category