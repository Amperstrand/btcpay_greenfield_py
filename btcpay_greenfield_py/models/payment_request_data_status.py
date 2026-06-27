from enum import Enum


class PaymentRequestDataStatus(str, Enum):
    COMPLETED = "Completed"
    EXPIRED = "Expired"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
