from typing import Optional

from pydantic import BaseModel, ConfigDict



class PathGetSketchTargetUuid(BaseModel):
    """The response from the `PathGetSketchTargetUuid` command."""

    target_id: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
