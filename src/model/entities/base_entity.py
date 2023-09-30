import uuid
from datetime import datetime

from pydantic import Field, BaseModel


class BaseEntity(BaseModel):
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
    name: str
    description: str
    date_added: datetime
    price: float = Field(ge=0)
