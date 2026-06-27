from enum import Enum


class SpeedPolicy(str, Enum):
    HIGHSPEED = "HighSpeed"
    LOWMEDIUMSPEED = "LowMediumSpeed"
    LOWSPEED = "LowSpeed"
    MEDIUMSPEED = "MediumSpeed"

    def __str__(self) -> str:
        return str(self.value)
