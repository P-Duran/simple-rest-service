from typing import List

from pydantic import Field

from model.dto.order_field import OrderField
from model.entities.base_entity import BaseEntity


class ProductEntity(BaseEntity):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    price: float = Field(ge=0)
    order_fields: List[OrderField]
