from enum import Enum


class AiPromptType(str, Enum):
    """A type of AI prompt."""  # noqa: E501

    """# Text to CAD. """  # noqa: E501
    TEXT_TO_CAD = "text_to_cad"
    """# Text to KCL. """  # noqa: E501
    TEXT_TO_KCL = "text_to_kcl"

    def __str__(self) -> str:
        return str(self.value)
