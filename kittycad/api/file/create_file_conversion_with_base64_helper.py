from typing import Any, Dict, Optional, Union

import base64
import httpx

from ...client import Client
from ...models import Error
from ...models import FileConversion
from ...models import FileImportFormat
from ...models import FileExportFormat
from ...types import Response
from ...api.file.create_file_conversion import sync as fc_sync, asyncio as fc_asyncio

def sync(
    src_format: FileImportFormat,
    output_format: FileExportFormat,
    body: bytes,
    *,
    client: Client,
) -> Optional[Union[Any, FileConversion, Error]]:
    """Convert a CAD file from one format to another. If the file being converted is larger than a certain size it will be performed asynchronously. This function automatically base64 encodes the request body and base64 decodes the request output."""

    encoded = base64.b64encode(body)

    fc = fc_sync(
        src_format=src_format,
        output_format=output_format,
        body=encoded,
        client=client,
    )

    if isinstance(fc, FileConversion) and fc.output != "":
        fc.output = base64.b64decode(fc.output)

    return fc


async def asyncio(
    src_format: FileImportFormat,
    output_format: FileExportFormat,
    body: bytes,
    *,
    client: Client,
) -> Optional[Union[Any, FileConversion, Error]]:
    """Convert a CAD file from one format to another. If the file being converted is larger than a certain size it will be performed asynchronously. This function automatically base64 encodes the request body and base64 decodes the request output."""

    encoded = base64.b64encode(body)

    fc = await fc_asyncio(
            src_format=src_format,
            output_format=output_format,
            body=encoded,
            client=client,
        )

    if isinstance(fc, FileConversion) and fc.output != "":
        fc.output = base64.b64decode(fc.output)

    return fc
