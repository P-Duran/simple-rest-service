from decorators.repository_decorators import repository
from model.entities.product_entity import ProductEntity
from repositories.base_repository import BaseRepository


@repository(ProductEntity)
class ProductRepository(BaseRepository[ProductEntity]):
    pass
