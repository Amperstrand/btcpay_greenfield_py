from enum import Enum


class PayoutState(str, Enum):
    AWAITINGAPPROVAL = "AwaitingApproval"
    AWAITINGPAYMENT = "AwaitingPayment"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    INPROGRESS = "InProgress"

    def __str__(self) -> str:
        return str(self.value)
