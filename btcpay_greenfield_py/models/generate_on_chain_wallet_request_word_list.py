from enum import Enum


class GenerateOnChainWalletRequestWordList(str, Enum):
    CHINESESIMPLIFIED = "ChineseSimplified"
    CHINESETRADITIONAL = "ChineseTraditional"
    CZECH = "Czech"
    ENGLISH = "English"
    FRENCH = "French"
    JAPANESE = "Japanese"
    PORTUGUESEBRAZIL = "PortugueseBrazil"
    SPANISH = "Spanish"

    def __str__(self) -> str:
        return str(self.value)
