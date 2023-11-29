from typing import List, Optional

from pydantic import BaseModel

from ..models.output_file import OutputFile


class CodeOutput(BaseModel):
    """Output of the code being executed."""

    output_files: Optional[List[OutputFile]] = None

    stderr: Optional[str] = None

    stdout: Optional[str] = None
