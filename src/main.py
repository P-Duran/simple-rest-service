from fastapi import FastAPI
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse

from repositories.order_repository import OrderRepository
from routes import product_router, order_router

app = FastAPI()

order_repository = OrderRepository()

app.include_router(product_router.router)
app.include_router(order_router.router)


@app.exception_handler(ValidationException)
async def validation_exception_handler(request, exc: ValidationException):
    return JSONResponse(
        status_code=400,
        content=exc.errors(),
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}
