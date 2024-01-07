from typing import List, Optional

from pydantic import BaseModel, ConfigDict



class IceServer(BaseModel):
    """Representation of an ICE server used for STUN/TURN Used to initiate WebRTC connections based on <https://developer.mozilla.org/en-US/docs/Web/API/RTCIceServer>"""

    credential: Optional[str] = None

    urls: List[str]

    username: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
