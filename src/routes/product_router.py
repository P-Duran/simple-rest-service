from uuid import UUID

from fastapi import APIRouter, HTTPException

from model.requests.product_request import ProductRequest
from services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("")
async def get_all():
    return ProductService().get_all()


@router.get("/{product_id}")
async def get_by_id(product_id: UUID):
    product = ProductService().get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Item not found")
    return product


@router.get("/active")
async def get_active_by_reservation(reservation_id: UUID):
    return ProductService().get_active_by_reservation(reservation_id)


@router.post("")
async def create(product: ProductRequest):
    return ProductService().create_new(product)
