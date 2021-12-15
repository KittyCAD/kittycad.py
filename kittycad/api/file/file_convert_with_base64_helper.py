from typing import Any, Dict, Optional, Union

import base64
import httpx

from ...client import AuthenticatedClient
from ...models.file_conversion import FileConversion
from ...models.valid_file_type import ValidFileType
from ...types import Response
from ...api.file.file_convert import sync as fc_sync, asyncio as fc_asyncio

def sync(
    source_format: ValidFileType,
    output_format: ValidFileType,
    content: bytes,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, FileConversion]]:
    """Convert a CAD file from one format to another. If the file being converted is larger than a certain size it will be performed asynchronously. This function automatically base64 encodes the request body and base64 decodes the request output."""

    encoded = base64.b64encode(content)

    fc = fc_sync(
        source_format=source_format,
        output_format=output_format,
        content=encoded,
        client=client,
    )

    if fc != None and fc.output != "":
        fc.output = base64.b64decode(fc.output)

    return fc


async def asyncio(
    source_format: ValidFileType,
    output_format: ValidFileType,
    content: bytes,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, FileConversion]]:
    """Convert a CAD file from one format to another. If the file being converted is larger than a certain size it will be performed asynchronously. This function automatically base64 encodes the request body and base64 decodes the request output."""

    encoded = base64.b64encode(content)

    fc = await fc_asyncio(
            source_format=source_format,
            output_format=output_format,
            content=encoded,
            client=client,
        )

    if fc != None and fc.output != "":
        fc.output = base64.b64decode(fc.output)

    return fc
