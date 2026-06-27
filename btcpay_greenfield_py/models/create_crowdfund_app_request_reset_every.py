from enum import Enum


class CreateCrowdfundAppRequestResetEvery(str, Enum):
    DAY = "Day"
    HOUR = "Hour"
    MONTH = "Month"
    NEVER = "Never"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
