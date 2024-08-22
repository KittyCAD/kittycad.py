from enum import Enum


class TextToCadModel(str, Enum):
    """A type of Text-to-CAD model."""  # noqa: E501

    """# CAD. """  # noqa: E501
    CAD = "cad"
    """# KCL. """  # noqa: E501
    KCL = "kcl"
    """# KCL iteration. """  # noqa: E501
    KCL_ITERATION = "kcl_iteration"

    def __str__(self) -> str:
        return str(self.value)
