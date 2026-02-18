from enum import Enum


class OrgDatasetFileConversionPhase(str, Enum):
    """Fine-grained pipeline stage for org dataset file conversions."""  # noqa: E501

    """# Phase index `0`: waiting for a worker to begin processing this conversion."""  # noqa: E501

    QUEUED = "queued"

    """# Phase index `1`: generating original file metadata."""  # noqa: E501

    ZOO_GENERATED_ORIGINAL_METADATA = "zoo_generated_original_metadata"

    """# Phase index `2`: creating a snapshot of the original source model."""  # noqa: E501

    SNAPSHOT_ORIGINAL = "snapshot_original"

    """# Phase index `3`: discovering optional user-provided metadata files (`.json`, `.yaml`, `.yml`, `.toml`, `.txt`) stored next to the source CAD file."""  # noqa: E501

    USER_PROVIDED_METADATA = "user_provided_metadata"

    """# Phase index `4`: converting the source model into raw KCL."""  # noqa: E501

    CONVERT_RAW_KCL = "convert_raw_kcl"

    """# Phase index `5`: generating raw KCL metadata."""  # noqa: E501

    ZOO_GENERATED_RAW_KCL_METADATA = "zoo_generated_raw_kcl_metadata"

    """# Phase index `6`: creating a snapshot of the raw KCL result."""  # noqa: E501

    SNAPSHOT_RAW_KCL = "snapshot_raw_kcl"

    """# Phase index `7`: running the salon/refactor step that produces polished KCL."""  # noqa: E501

    SALON = "salon"

    """# Phase index `8`: generating salon KCL metadata."""  # noqa: E501

    ZOO_GENERATED_SALON_KCL_METADATA = "zoo_generated_salon_kcl_metadata"

    """# Phase index `9`: creating a snapshot of the salon/refactored KCL."""  # noqa: E501

    SNAPSHOT_SALON_KCL = "snapshot_salon_kcl"

    """# Phase index `10`: conversion finished successfully."""  # noqa: E501

    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
