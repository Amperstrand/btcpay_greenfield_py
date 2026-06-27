from enum import Enum


class CreatePointOfSaleAppRequestDefaultView(str, Enum):
    CART = "Cart"
    LIGHT = "Light"
    PRINT = "Print"
    STATIC = "Static"

    def __str__(self) -> str:
        return str(self.value)
