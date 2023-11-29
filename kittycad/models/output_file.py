from typing import Optional

from pydantic import BaseModel



class OutputFile(BaseModel):
    """Output file contents."""

    contents: Optional[str] = None

    name: Optional[str] = None
