from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse

from model.dto.order_field import OrderField
from model.enums.order_field_type import OrderFieldType
from model.requests.product_request import ProductRequest
from repositories.order_repository import OrderRepository
from routes import product_router, order_router
from services.product_service import ProductService


@asynccontextmanager
async def lifespan(app: FastAPI):
    ProductService().create_new(
        ProductRequest(name="Surf", description="Clases de surf en Bastiagueiro", price=25,
                       order_fields=[OrderField(name="date", type=OrderFieldType.Date),
                                     OrderField(name="time", type=OrderFieldType.Time),
                                     OrderField(name="additional_notes",
                                                type=OrderFieldType.String)]))
    ProductService().create_new(
        ProductRequest(name="Desayuno", description="Desyuno en el hotel Pueblo Paleta", price=10,
                       order_fields=[OrderField(name="date", type=OrderFieldType.Date),
                                     OrderField(name="breakfast_type", type=OrderFieldType.String)]))
    yield


app = FastAPI(lifespan=lifespan)

order_repository = OrderRepository()

app.include_router(product_router.router)
app.include_router(order_router.router)


@app.exception_handler(ValidationException)
async def validation_exception_handler(request, exc: ValidationException):
    return JSONResponse(
        status_code=400,
        content=exc.errors(),
    )
