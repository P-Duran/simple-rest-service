from fastapi import FastAPI

from model.entities.order_entity import OrderEntity
from model.entities.product_entity import ProductEntity
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository

app = FastAPI()

product_repository = ProductRepository()
order_repository = OrderRepository()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/find_all")
async def find_all():
    return product_repository.find_all()


@app.post("/create")
async def create(product: ProductEntity):
    return product_repository.add(product)


@app.get("/orders/find_all")
async def find_all():
    return order_repository.find_all()


@app.post("/orders/create")
async def create(order: OrderEntity):
    return order_repository.add(order)
