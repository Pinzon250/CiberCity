from fastapi import FastAPI
from app.routes.auth import users
from app.database.connection import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def home():
    return {"msg": "ta funcionando"}