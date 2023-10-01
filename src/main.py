from fastapi import FastAPI

from repositories.order_repository import OrderRepository
from routes import product_router, order_router

app = FastAPI()

order_repository = OrderRepository()

app.include_router(product_router.router)
app.include_router(order_router.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
