from typing import Optional

from .base import KittyCadBaseModel


class MlCopilotModeOption(KittyCadBaseModel):
    """A client-facing ML copilot mode option."""

    description: str

    disabled: Optional[bool] = False

    icon: str

    id: str

    label: str
