from enum import Enum


class OrgDatasetFileConversionStatus(str, Enum):
    """`OrgDatasetFileConversion` status."""  # noqa: E501

    """# Pending conversion."""  # noqa: E501

    QUEUED = "queued"

    """# The file will not be converted."""  # noqa: E501

    CANCELED = "canceled"

    """# The file is currently being converted. If `started_at` passes a certain threshold, we assume it got dropped and will retry."""  # noqa: E501

    IN_PROGRESS = "in_progress"

    """# Conversion finished with the result available at `output_path`."""  # noqa: E501

    SUCCESS = "success"

    """# Conversion failed due to user providing a broken file, such as it being empty."""  # noqa: E501

    ERROR_USER = "error_user"

    """# Conversion failed because we didn't know how to handle the file. The conversion should be retried with a new converter version."""  # noqa: E501

    ERROR_UNSUPPORTED = "error_unsupported"

    """# Conversion failed with some other unrecoverable error. The conversion should be retried with a new converter version."""  # noqa: E501

    ERROR_INTERNAL = "error_internal"

    def __str__(self) -> str:
        return str(self.value)
