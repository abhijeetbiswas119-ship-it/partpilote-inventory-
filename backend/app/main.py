

from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine
from app.db.init_db import init_db
from app.routers import inventory
from app.routers import inventory
from app.routers import category
from app.routers import auth

# Create FastAPI app
app = FastAPI(
    title="PartPilot API",
    version="1.0.0"
)

# Create database tables
init_db()

# Include routers
app.include_router(inventory.router)
app.include_router(category.router)
app.include_router(auth.router)


@app.get("/")
def root():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "message": "PartPilot API connected to Supabase successfully"
        }

    except Exception as e:
        return {
            "error": str(e)
        }