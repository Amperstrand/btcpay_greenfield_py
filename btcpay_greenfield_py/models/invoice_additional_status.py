from enum import Enum


class InvoiceAdditionalStatus(str, Enum):
    INVALID = "Invalid"
    MARKED = "Marked"
    NONE = "None"
    PAIDLATE = "PaidLate"
    PAIDOVER = "PaidOver"
    PAIDPARTIAL = "PaidPartial"

    def __str__(self) -> str:
        return str(self.value)
