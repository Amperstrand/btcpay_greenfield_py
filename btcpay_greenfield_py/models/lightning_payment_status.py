from enum import Enum


class LightningPaymentStatus(str, Enum):
    COMPLETE = "Complete"
    FAILED = "Failed"
    PENDING = "Pending"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
