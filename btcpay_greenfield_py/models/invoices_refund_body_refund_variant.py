from enum import Enum


class InvoicesRefundBodyRefundVariant(str, Enum):
    CURRENTRATE = "CurrentRate"
    CUSTOM = "Custom"
    FIAT = "Fiat"
    OVERPAIDAMOUNT = "OverpaidAmount"
    RATETHEN = "RateThen"

    def __str__(self) -> str:
        return str(self.value)
