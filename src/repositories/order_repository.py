from decorators.repository_decorators import repository
from model.entities.order_entity import OrderEntity
from repositories.base_repository import BaseRepository


@repository(OrderEntity)
class OrderRepository(BaseRepository[OrderEntity]):
    pass
