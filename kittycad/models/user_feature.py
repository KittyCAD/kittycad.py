from enum import Enum


class UserFeature(str, Enum):
    BODIES_PANE = "bodies_pane"

    ENABLE_Z0006_LINT = "enable_z0006_lint"

    MODELING_DIALOGS = "modeling_dialogs"

    PLUGINS = "plugins"

    PROPRIETARY_TO_KCL_CONVERSION_BETA = "proprietary_to_kcl_conversion_beta"

    SEGMENTS_BASED_REGIONS = "segments_based_regions"

    SKETCH_EXPERIMENTAL_FEATURES = "sketch_experimental_features"

    WEB_APP_FILE_BROWSER = "web_app_file_browser"

    def __str__(self) -> str:
        return str(self.value)
