from typing import List
from uuid import UUID

from pydantic import BaseModel

from model.dto.order_field_value import OrderFieldValue


class OrderRequest(BaseModel):
    reservation_id: UUID
    product_id: UUID
    fields: List[OrderFieldValue]
