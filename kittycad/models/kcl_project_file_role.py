from enum import Enum


class KclProjectFileRole(str, Enum):
    """Logical role of a file stored under a KCL project."""  # noqa: E501

    """# The root `project.toml` manifest."""  # noqa: E501

    PROJECT_TOML = "project_toml"

    """# A project source file such as `.kcl`."""  # noqa: E501

    PROJECT_FILE = "project_file"

    """# A preview image generated or uploaded for the gallery."""  # noqa: E501

    PREVIEW_IMAGE = "preview_image"

    def __str__(self) -> str:
        return str(self.value)
