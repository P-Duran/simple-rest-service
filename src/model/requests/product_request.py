from typing import List

from pydantic import Field, BaseModel

from model.dto.order_field import OrderField


class ProductRequest(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    price: float = Field(ge=0)
    order_fields: List[OrderField]
