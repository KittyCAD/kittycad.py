from enum import Enum


class WorldCoordinateSystem(str, Enum):
    RIGHT_HANDED_UP_Z = "right_handed_up_z"

    RIGHT_HANDED_UP_Y = "right_handed_up_y"

    def __str__(self) -> str:
        return str(self.value)
