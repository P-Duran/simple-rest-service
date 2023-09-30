from datetime import datetime

from pydantic import Field

from model.entities.base_entity import BaseEntity


class ProductEntity(BaseEntity):
    name: str
    description: str
    date_added: datetime
    price: float = Field(ge=0)
