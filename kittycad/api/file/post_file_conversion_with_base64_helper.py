from typing import Any, Dict, Optional, Union

import base64
import httpx

from ...client import Client
from ...models.error_message import ErrorMessage
from ...models.file_conversion import FileConversion
from ...models.valid_source_file_format import ValidSourceFileFormat
from ...models.valid_output_file_format import ValidOutputFileFormat
from ...types import Response
from ...api.file.post_file_conversion import sync as fc_sync, asyncio as fc_asyncio

def sync(
    source_format: ValidSourceFileFormat,
    output_format: ValidOutputFileFormat,
    body: bytes,
    *,
    client: Client,
) -> Optional[Union[Any, FileConversion, ErrorMessage]]:
    """Convert a CAD file from one format to another. If the file being converted is larger than a certain size it will be performed asynchronously. This function automatically base64 encodes the request body and base64 decodes the request output."""

    encoded = base64.b64encode(body)

    fc = fc_sync(
        source_format=source_format,
        output_format=output_format,
        body=encoded,
        client=client,
    )

    if isinstance(fc, FileConversion) and fc.output != "":
        fc.output = base64.b64decode(fc.output)

    return fc


async def asyncio(
    source_format: ValidSourceFileFormat,
    output_format: ValidOutputFileFormat,
    body: bytes,
    *,
    client: Client,
) -> Optional[Union[Any, FileConversion, ErrorMessage]]:
    """Convert a CAD file from one format to another. If the file being converted is larger than a certain size it will be performed asynchronously. This function automatically base64 encodes the request body and base64 decodes the request output."""

    encoded = base64.b64encode(body)

    fc = await fc_asyncio(
            source_format=source_format,
            output_format=output_format,
            body=encoded,
            client=client,
        )

    if isinstance(fc, FileConversion) and fc.output != "":
        fc.output = base64.b64decode(fc.output)

    return fc
