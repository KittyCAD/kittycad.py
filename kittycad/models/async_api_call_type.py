from enum import Enum


class AsyncApiCallType(str, Enum):
    """The type of async API call."""  # noqa: E501

    """# File conversion. """  # noqa: E501
    FILE_CONVERSION = "file_conversion"
    """# File volume. """  # noqa: E501
    FILE_VOLUME = "file_volume"
    """# File center of mass. """  # noqa: E501
    FILE_CENTER_OF_MASS = "file_center_of_mass"
    """# File mass. """  # noqa: E501
    FILE_MASS = "file_mass"
    """# File density. """  # noqa: E501
    FILE_DENSITY = "file_density"
    """# File surface area. """  # noqa: E501
    FILE_SURFACE_AREA = "file_surface_area"
    """# Text to CAD. """  # noqa: E501
    TEXT_TO_CAD = "text_to_cad"

    def __str__(self) -> str:
        return str(self.value)
