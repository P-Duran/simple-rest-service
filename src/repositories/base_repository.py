import uuid

from typing import Generic, TypeVar, Type, List, Optional

T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, element_class: Type[T]):
        self.element_class = element_class
        self.db = {}

    def find_all(self) -> List[T]:
        return self.db.get(self.element_class)

    def find_by_id(self, element_id: uuid) -> Optional[T]:
        return self.db.get(self.element_class, {}).get(element_id)

    def add(self, element: T):
        self.db[self.element_class] = {**(self.db[self.element_class] if self.element_class in self.db else {}),
                                       element.id: element}
