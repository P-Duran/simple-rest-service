import uuid
from typing import Generic, TypeVar, List, Optional

from utils.singleton import SingletonMeta

T = TypeVar("T")


class BaseRepository(Generic[T], metaclass=SingletonMeta):
    def __init__(self):
        self.db = {}

    def find_all(self) -> List[T]:
        return list(self.db.values())

    def find_by_id(self, element_id: uuid) -> Optional[T]:
        return self.db.get(element_id)

    def add(self, element: T):
        self.db[element.id] = element
        return element
