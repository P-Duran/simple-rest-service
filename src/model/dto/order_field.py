from pydantic import BaseModel

from model.enums.order_field_type import OrderFieldType


class OrderField(BaseModel):
    name: str
    type: OrderFieldType
