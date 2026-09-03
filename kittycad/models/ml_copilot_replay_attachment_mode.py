from enum import Enum


class MlCopilotReplayAttachmentMode(str, Enum):
    """Controls whether replayed attachments are sent inline or fetched on demand."""  # noqa: E501

    """# Include full attachment bytes in replayed files."""  # noqa: E501

    FULL = "full"

    """# Omit attachment bytes and include only socket fetch metadata."""  # noqa: E501

    METADATA_ONLY = "metadata_only"

    def __str__(self) -> str:
        return str(self.value)
