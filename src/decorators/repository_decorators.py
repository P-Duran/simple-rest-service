from typing import Type

from model.entities.base_entity import BaseEntity


def repository(element: Type[BaseEntity]):
    def internal_repository(original_class):
        orig_init = original_class.__init__

        def __init__(self, *args, **kws):
            orig_init(self, element, *args, **kws)
            super(original_class, self).__init__(element)

        original_class.__init__ = __init__
        return original_class

    return internal_repository
