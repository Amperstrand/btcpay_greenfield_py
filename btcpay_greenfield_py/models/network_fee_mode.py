from enum import Enum


class NetworkFeeMode(str, Enum):
    ALWAYS = "Always"
    MULTIPLEPAYMENTSONLY = "MultiplePaymentsOnly"
    NEVER = "Never"

    def __str__(self) -> str:
        return str(self.value)
