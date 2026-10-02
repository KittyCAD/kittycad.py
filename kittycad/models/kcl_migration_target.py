from enum import Enum


class KclMigrationTarget(str, Enum):
    """A supported migration target. Preview use always requires explicit consent."""  # noqa: E501

    """# Unstable KCL 3 preview."""  # noqa: E501

    VAL_3_0_PREVIEW = "3.0-preview"

    """# Stable KCL 3. Availability also depends on the deployed worker and client."""  # noqa: E501

    VAL_3_0 = "3.0"

    def __str__(self) -> str:
        return str(self.value)
