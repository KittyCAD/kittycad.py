from enum import Enum


class ProjectArchiveFormat(str, Enum):
    """Archive formats supported by project download endpoints."""  # noqa: E501

    """# Return a tar archive."""  # noqa: E501

    TAR = "tar"

    """# Return a zip archive."""  # noqa: E501

    ZIP = "zip"

    def __str__(self) -> str:
        return str(self.value)
