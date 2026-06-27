from enum import Enum


class CheckoutOptionsCheckoutTypeType3Type1(str, Enum):
    V1 = "V1"
    V2 = "V2"

    def __str__(self) -> str:
        return str(self.value)
