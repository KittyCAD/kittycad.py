from enum import Enum


class ZooTool(str, Enum):
    """The Zoo tools that can make API calls."""  # noqa: E501

    """# Design Studio and verified Zookeeper callbacks."""  # noqa: E501

    MODELING_APP = "modeling_app"

    """# Legacy Text-to-CAD entitlement, retained for existing plan records."""  # noqa: E501

    TEXT_TO_CAD = "text_to_cad"

    def __str__(self) -> str:
        return str(self.value)
