from enum import Enum


class ZooTool(str, Enum):
    """The Zoo tools that can make API calls."""  # noqa: E501

    """# The modeling app. """  # noqa: E501
    MODELING_APP = "modeling_app"
    """# The Text-to-CAD UI. """  # noqa: E501
    TEXT_TO_CAD = "text_to_cad"
    """# The Diff Chrome Extension. """  # noqa: E501
    DIFF_CHROME_EXTENSION = "diff_chrome_extension"

    def __str__(self) -> str:
        return str(self.value)
