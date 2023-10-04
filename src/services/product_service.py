from uuid import UUID

from fastapi.exceptions import ValidationException

from model.dto.enriched_product import EnrichedProduct
from model.entities.product_entity import ProductEntity
from model.requests.product_request import ProductRequest
from repositories.product_repository import ProductRepository
from services.order_service import OrderService


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
        if order_by is None:
            order_by = "date_added"
            # It would be nice to have the name of the field taken from the class itself instead,
            # but it is not easy to do in a simple way, and in this way is really readable what is happening

        if order_by not in EnrichedProduct.model_fields.keys():
            raise ValidationException(errors=[
                f"The order_by field '{order_by}' is not one of the following {EnrichedProduct.model_fields.keys()}"])
        return sorted(
            [EnrichedProduct(**p.__dict__, orders=len(self._order_service.get_orders_by_product(p.id))) for p in
             self._product_repository.find_all()], key=lambda p: p.__dict__[order_by])

    def get_by_reservation(self, reservation_id: UUID):
        orders = self._order_service.get_orders_by_reservation(reservation_id)

        active_products = []
        for order in orders:
            active_products.append(self._product_repository.find_by_id(order.product_id))
        return active_products
