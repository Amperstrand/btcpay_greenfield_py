from enum import Enum


class CheckoutType(str, Enum):
    V1 = "V1"
    V2 = "V2"

    def __str__(self) -> str:
        return str(self.value)
