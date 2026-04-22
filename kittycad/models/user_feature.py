from enum import Enum


class UserFeature(str, Enum):
    AQUARIUM = "aquarium"

    PROPRIETARY_TO_KCL_CONVERSION_BETA = "proprietary_to_kcl_conversion_beta"

    CLASSIC_SKETCH_MODE = "classic_sketch_mode"

    WEB_APP_FILE_BROWSER = "web_app_file_browser"

    def __str__(self) -> str:
        return str(self.value)
