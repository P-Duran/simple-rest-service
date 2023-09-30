from typing import Any

from pydantic import BaseModel


class OrderFieldValue(BaseModel):
    field: str
    value: Any
