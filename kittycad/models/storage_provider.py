from enum import Enum


class StorageProvider(str, Enum):
    """Storage provider identifier for org datasets."""  # noqa: E501

    """# Amazon Simple Storage Service."""  # noqa: E501

    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
