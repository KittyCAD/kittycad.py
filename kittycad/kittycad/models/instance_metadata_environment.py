from enum import Enum


class InstanceMetadataEnvironment(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    PREVIEW = "PREVIEW"
    PRODUCTION = "PRODUCTION"

    def __str__(self) -> str:
        return str(self.value)
