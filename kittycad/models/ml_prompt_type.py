from enum import Enum


class MlPromptType(str, Enum):
    """A type of ML prompt."""  # noqa: E501

    """# Text to CAD. """  # noqa: E501
    TEXT_TO_CAD = "text_to_cad"
    """# Text to KCL. """  # noqa: E501
    TEXT_TO_KCL = "text_to_kcl"
    """# Text to Kcl iteration, """  # noqa: E501
    TEXT_TO_KCL_ITERATION = "text_to_kcl_iteration"

    def __str__(self) -> str:
        return str(self.value)
