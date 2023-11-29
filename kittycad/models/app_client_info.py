from typing import Optional

from pydantic import BaseModel



class AppClientInfo(BaseModel):
    """Information about a third party app client."""

    url: Optional[str] = None
