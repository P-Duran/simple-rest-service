from typing import List
from uuid import UUID

from model.dto.order_field_value import OrderFieldValue
from model.entities.base_entity import BaseEntity


class OrderEntity(BaseEntity):
    reservation_id: UUID
    product_id: UUID
    fields: List[OrderFieldValue]
