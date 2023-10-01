from typing import List

from pydantic import Field, BaseModel

from model.dto.order_field import OrderField


class ProductRequest(BaseModel):
    name: str
    description: str
    price: float = Field(ge=0)
    order_fields: List[OrderField]
