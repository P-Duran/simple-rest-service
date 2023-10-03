from model.entities.product_entity import ProductEntity


class EnrichedProduct(ProductEntity):
    orders: int
