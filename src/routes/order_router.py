from fastapi import APIRouter
from starlette.responses import JSONResponse

from model.requests.order_request import OrderRequest
from services.order_service import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("")
async def get_all():
    return OrderService().get_all()


@router.post("")
async def create(order: OrderRequest):
    validation_errors = OrderService().create(order)
    if len(validation_errors) != 0:
        return JSONResponse(content=validation_errors, status_code=400)
