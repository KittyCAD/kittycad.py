from enum import Enum


class StorageProvider(str, Enum):
    """Storage provider identifier for org datasets."""  # noqa: E501

    """# Amazon Simple Storage Service."""  # noqa: E501

    S3 = "s3"

    """# Zoo-managed dataset storage backed by the API's internal object store."""  # noqa: E501

    ZOO_MANAGED = "zoo_managed"

    def __str__(self) -> str:
        return str(self.value)
