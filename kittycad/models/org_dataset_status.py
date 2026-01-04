from enum import Enum


class OrgDatasetStatus(str, Enum):
    """Lifecycle status for org datasets."""  # noqa: E501

    """# Dataset is active and can be used."""  # noqa: E501

    ACTIVE = "active"

    """# Dataset is being deleted and should not be mutated or used."""  # noqa: E501

    DELETING = "deleting"

    """# Dataset encountered sync errors and needs attention."""  # noqa: E501

    ERRORED = "errored"

    def __str__(self) -> str:
        return str(self.value)
