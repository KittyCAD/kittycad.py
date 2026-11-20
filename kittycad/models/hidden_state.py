from enum import Enum


class HiddenState(str, Enum):
    """Visibility of an object, or whether the requested object does not exist."""  # noqa: E501

    """# The object exists and is hidden."""  # noqa: E501

    HIDDEN = "hidden"

    """# The object exists and is visible."""  # noqa: E501

    VISIBLE = "visible"

    """# No object exists for the requested UUID."""  # noqa: E501

    NO_SUCH_OBJECT = "no_such_object"

    def __str__(self) -> str:
        return str(self.value)
