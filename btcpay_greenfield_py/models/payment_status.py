from enum import Enum


class PaymentStatus(str, Enum):
    INVALID = "Invalid"
    PROCESSING = "Processing"
    SETTLED = "Settled"

    def __str__(self) -> str:
        return str(self.value)
