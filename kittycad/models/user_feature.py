from enum import Enum


class UserFeature(str, Enum):
    PROPRIETARY_TO_KCL_CONVERSION_BETA = "proprietary_to_kcl_conversion_beta"

    NEW_SKETCH_MODE = "new_sketch_mode"

    def __str__(self) -> str:
        return str(self.value)
