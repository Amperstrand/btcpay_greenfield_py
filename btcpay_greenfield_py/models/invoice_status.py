from enum import Enum


class InvoiceStatus(str, Enum):
    EXPIRED = "Expired"
    INVALID = "Invalid"
    NEW = "New"
    PROCESSING = "Processing"
    SETTLED = "Settled"

    def __str__(self) -> str:
        return str(self.value)
