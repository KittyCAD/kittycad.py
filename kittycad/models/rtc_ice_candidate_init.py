from typing import Optional

from pydantic import BaseModel, ConfigDict



class RtcIceCandidateInit(BaseModel):
    """ICECandidateInit is used to serialize ice candidates"""

    candidate: str

    sdpMLineIndex: Optional[int] = None

    sdpMid: Optional[str] = None

    usernameFragment: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
