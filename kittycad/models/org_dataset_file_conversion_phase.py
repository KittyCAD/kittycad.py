from enum import Enum


class OrgDatasetFileConversionPhase(str, Enum):
    """Fine-grained pipeline stage for org dataset file conversions."""  # noqa: E501

    """# Phase index `0`: waiting for a worker to begin processing this conversion."""  # noqa: E501

    QUEUED = "queued"

    """# Phase index `1`: creating a snapshot of the original source model."""  # noqa: E501

    SNAPSHOT_ORIGINAL = "snapshot_original"

    """# Phase index `2`: converting the source model into raw KCL."""  # noqa: E501

    CONVERT_RAW_KCL = "convert_raw_kcl"

    """# Phase index `3`: creating a snapshot of the raw KCL result."""  # noqa: E501

    SNAPSHOT_RAW_KCL = "snapshot_raw_kcl"

    """# Phase index `4`: running the salon/refactor step that produces polished KCL."""  # noqa: E501

    SALON = "salon"

    """# Phase index `5`: creating a snapshot of the salon/refactored KCL."""  # noqa: E501

    SNAPSHOT_SALON_KCL = "snapshot_salon_kcl"

    """# Phase index `6`: conversion finished successfully."""  # noqa: E501

    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
