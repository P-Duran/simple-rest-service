from fastapi import APIRouter

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
    return OrderService().create(order)
