from datetime import datetime

from model.entities.base_entity import BaseEntity
from model.enums.breakfast_type import BreakfastType


class SurfEntity(BaseEntity):
    date: datetime
    breakfast_type: BreakfastType
