

from app.db.init_db import init_db

from fastapi import FastAPI

app = FastAPI()
init_db()


@app.get("/")
def root():
    return {
        "message": "Welcome to PartPilot API"
    }