from enum import Enum


class MlPromptType(str, Enum):
    """A type of ML prompt."""  # noqa: E501

    """# Text to CAD."""  # noqa: E501

    TEXT_TO_CAD = "text_to_cad"

    """# Text to KCL."""  # noqa: E501

    TEXT_TO_KCL = "text_to_kcl"

    """# Text to KCL iteration."""  # noqa: E501

    TEXT_TO_KCL_ITERATION = "text_to_kcl_iteration"

    """# Text to KCL iteration with multiple files."""  # noqa: E501

    TEXT_TO_KCL_MULTI_FILE_ITERATION = "text_to_kcl_multi_file_iteration"

    """# Copilot chat/assist prompts."""  # noqa: E501

    COPILOT = "copilot"

    def __str__(self) -> str:
        return str(self.value)
