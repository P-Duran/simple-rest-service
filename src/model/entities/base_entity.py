import uuid

from pydantic import Field, BaseModel


class BaseEntity(BaseModel):
    id: uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
