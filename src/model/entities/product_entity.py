from datetime import datetime
from typing import List

from pydantic import Field

from model.dto.order_field import OrderField
from model.entities.base_entity import BaseEntity


class ProductEntity(BaseEntity):
    name: str
    description: str
    date_added: datetime
    price: float = Field(ge=0)
    order_fields: List[OrderField]
