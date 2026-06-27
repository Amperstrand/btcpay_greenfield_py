from enum import Enum


class InvoiceStatusMark(str, Enum):
    INVALID = "Invalid"
    SETTLED = "Settled"

    def __str__(self) -> str:
        return str(self.value)
