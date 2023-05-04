import base64
from typing import Any, Optional, Union

from ...api.api_calls.get_async_operation import asyncio as fc_asyncio, sync as fc_sync
from ...client import Client
from ...models import Error
from ...models.file_conversion import FileConversion


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[Union[Any, FileConversion, Error]]:
    """Get the status of a file conversion. This function automatically base64 decodes the output response if there is one."""

    fc = fc_sync(
        id=id,
        client=client,
    )

    if isinstance(fc, FileConversion) and fc.output != "":
        if isinstance(fc.output, str):
            b = base64.b64decode(fc.output)
            # decode the bytes to a string
            fc.output = b.decode("utf-8")

    return fc


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[Union[Any, FileConversion, Error]]:
    """Get the status of a file conversion. This function automatically base64 decodes the output response if there is one."""

    fc = await fc_asyncio(
        id=id,
        client=client,
    )

    if isinstance(fc, FileConversion) and fc.output != "":
        if isinstance(fc.output, str):
            b = base64.b64decode(fc.output)
            # decode the bytes to a string
            fc.output = b.decode("utf-8")

    return fc
