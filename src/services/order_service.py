from typing import List
from uuid import UUID

from model.entities.order_entity import OrderEntity
from model.requests.order_request import OrderRequest
from repositories.order_repository import OrderRepository
from services.order_validation_service import OrderValidationService


class OrderService:

    def __init__(self):
        self._order_repository = OrderRepository()
        self._order_validation_service = OrderValidationService()

    def create(self, order: OrderRequest):
        self._order_validation_service.validate(order)
        return self._order_repository.add(OrderEntity(**order.__dict__))

    def get_all(self):
        return self._order_repository.find_all()

    def get_orders_by_reservation(self, reservation_id: UUID) -> List[OrderEntity]:
        return [order for order in self._order_repository.find_all() if order.reservation_id == reservation_id]

    def get_orders_by_product(self, product_id: UUID) -> List[OrderEntity]:
        return [order for order in self._order_repository.find_all() if order.product_id == product_id]
