from enum import Enum


class LightningInvoiceStatus(str, Enum):
    EXPIRED = "Expired"
    PAID = "Paid"
    UNPAID = "Unpaid"

    def __str__(self) -> str:
        return str(self.value)
