from enum import Enum


class InvoiceType(str, Enum):
    STANDARD = "Standard"
    TOPUP = "TopUp"

    def __str__(self) -> str:
        return str(self.value)
