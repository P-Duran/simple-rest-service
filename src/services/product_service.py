from uuid import UUID

from fastapi.exceptions import ValidationException

from model.dto.enriched_product import EnrichedProduct
from model.entities.product_entity import ProductEntity
from model.requests.product_request import ProductRequest
from repositories.product_repository import ProductRepository
from services.order_service import OrderService


def _order_by(product: EnrichedProduct, field: str):
    if field and field not in EnrichedProduct.model_fields.keys():
        raise ValidationException(errors=[
            f"The order_by field '{field}' is not one of the following {EnrichedProduct.model_fields.keys()}"])

    return product.date_added if field is None else product.__dict__[field]


class ProductService:
    def __init__(self):
        self._product_repository = ProductRepository()
        self._order_service = OrderService()

    def create_new(self, product: ProductRequest):
        return self._product_repository.add(ProductEntity(**product.__dict__))

    def get_by_id(self, id: UUID):
        product = self._product_repository.find_by_id(id)
        if product:
            return EnrichedProduct(**product.__dict__,
                                   orders=len(self._order_service.get_orders_by_product(product.id)))
        return None

    def get_all(self, order_by: str = None):
        return sorted(
            [EnrichedProduct(**p.__dict__, orders=len(self._order_service.get_orders_by_product(p.id))) for p in
             self._product_repository.find_all()], key=lambda p: _order_by(p, order_by), reverse=True)

    def get_by_reservation(self, reservation_id: UUID):
        orders = self._order_service.get_orders_by_reservation(reservation_id)

        active_products = []
        for order in orders:
            active_products.append(self._product_repository.find_by_id(order.product_id))
        return active_products
