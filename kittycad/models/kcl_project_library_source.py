from enum import Enum


class KclProjectLibrarySource(str, Enum):
    """Application that created a cloud project library."""  # noqa: E501

    """# Created through Zoo Design Studio. Also the default."""  # noqa: E501

    ZDS = "zds"

    """# Created through Factory Portal."""  # noqa: E501

    FACTORY_PORTAL = "factory_portal"

    """# Created by organization dataset conversion automation."""  # noqa: E501

    ORG_DATASET = "org_dataset"

    def __str__(self) -> str:
        return str(self.value)
