import uuid
from datetime import datetime

from pydantic import Field, BaseModel


class BaseEntity(BaseModel):
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
    date_added: datetime = Field(default_factory=lambda: datetime.now())
