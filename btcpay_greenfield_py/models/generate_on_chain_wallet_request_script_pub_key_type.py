from enum import Enum


class GenerateOnChainWalletRequestScriptPubKeyType(str, Enum):
    LEGACY = "Legacy"
    SEGWIT = "Segwit"
    SEGWITP2SH = "SegwitP2SH"

    def __str__(self) -> str:
        return str(self.value)
