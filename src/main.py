from fastapi import FastAPI

from model.entities.product_entity import ProductEntity
from repositories.product_repository import ProductRepository

app = FastAPI()

product_repository = ProductRepository()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/find_all")
async def find_all():
    return product_repository.find_all()


@app.post("/create")
async def create(product: ProductEntity):
    return product_repository.add(product)
