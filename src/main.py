from fastapi import FastAPI
from fastapi.responses import JSONResponse

from model.entities.order_entity import OrderEntity
from model.entities.product_entity import ProductEntity
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from services.order_validation_service import OrderValidationService

app = FastAPI()

product_repository = ProductRepository()
order_repository = OrderRepository()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/find_all")
async def find_all():
    return ProductRepository().find_all()


@app.post("/create")
async def create(product: ProductEntity):
    return ProductRepository().add(product)


@app.get("/orders/find_all")
async def find_all():
    return order_repository.find_all()


@app.post("/orders/create")
async def create(order: OrderEntity):
    validation_errors = OrderValidationService().validate(order)
    if len(validation_errors) != 0:
        return JSONResponse(content=validation_errors, status_code=404)
    return order_repository.add(order)
