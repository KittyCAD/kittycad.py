from enum import Enum


class PostEffectType(str, Enum):
    """Post effect type"""  # noqa: E501

    PHOSPHOR = "phosphor"
    SSAO = "ssao"
    NOEFFECT = "noeffect"

    def __str__(self) -> str:
        return str(self.value)
