from typing import Optional

from .base import KittyCadBaseModel


class PathGetSketchTargetUuid(KittyCadBaseModel):
    """The response from the `PathGetSketchTargetUuid` command."""

    target_id: Optional[str] = None
