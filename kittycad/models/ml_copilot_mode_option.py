from .base import KittyCadBaseModel


class MlCopilotModeOption(KittyCadBaseModel):
    """A client-facing ML copilot mode option."""

    description: str

    icon: str

    id: str

    label: str
