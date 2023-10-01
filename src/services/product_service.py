from uuid import UUID

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
        return self._product_repository.find_by_id(id)

    def get_all(self):
        return self._product_repository.find_all()

    def get_active_by_reservation(self, reservation_id: UUID):
        orders = self._order_service.get_orders_by_reservation(reservation_id)

        active_products = []
        for order in orders:
            popularity = len(self._order_service.get_orders_by_product(order.product_id))
            active_products.append(self._product_repository.find_by_id(order.product_id))
        return active_products.sort(key=lambda p: p.date_added)
