from fastapi.exceptions import ValidationException

from model.requests.order_request import OrderRequest
from repositories.product_repository import ProductRepository


class OrderValidationService:

    def __init__(self):
        self._product_repository = ProductRepository()

    def validate(self, order: OrderRequest):
        validation_errors = []
        product = self._product_repository.find_by_id(order.product_id)
        if product:
            for order_field in order.fields:
                product_field = next((f for f in product.order_fields if f.name == order_field.field), None)
                if not product_field:
                    validation_errors.append(
                        f"Order field '{order_field.field}' does not exist in product '{product.id}'")
                elif not product_field.type.validate(order_field.value):
                    validation_errors.append(
                        f"Order field value '{order_field.value}' does not match the type '{product_field.type}'")
        else:
            validation_errors.append(f"Product with id '{order.product_id}' not found")

        if len(validation_errors) != 0:
            raise ValidationException(errors=validation_errors)
