from enum import Enum


class TransactionStatus(str, Enum):
    CONFIRMED = "Confirmed"
    UNCONFIRMED = "Unconfirmed"

    def __str__(self) -> str:
        return str(self.value)
