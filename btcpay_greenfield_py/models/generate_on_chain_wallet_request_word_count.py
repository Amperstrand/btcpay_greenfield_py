from enum import IntEnum


class GenerateOnChainWalletRequestWordCount(IntEnum):
    VALUE_12 = 12
    VALUE_15 = 15
    VALUE_18 = 18
    VALUE_21 = 21
    VALUE_24 = 24

    def __str__(self) -> str:
        return str(self.value)
