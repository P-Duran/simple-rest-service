from uuid import UUID

from fastapi import APIRouter

from model.requests.product_request import ProductRequest
from services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("")
async def get_all():
    return ProductService().get_all()


@router.get("/active")
async def get_active_by_reservation(reservation_id: UUID):
    return ProductService().get_active_by_reservation(reservation_id)


@router.post("")
async def create(product: ProductRequest):
    return ProductService().create_new(product)
