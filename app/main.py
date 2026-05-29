from fastapi import FastAPI

from app.database.connection import engine, Base
from app.models.product import Product
from app.routers.product_router import router as product_router

app = FastAPI()

app.include_router(product_router)


Base.metadata.create_all(bind=engine)



@app.get("/")
def home():
    return {"message": "ZYRO Backend Running"}