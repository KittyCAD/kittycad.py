import base64
from typing import Any, Optional, Union

from ...api.file.get_file_conversion import asyncio as fc_asyncio
from ...api.file.get_file_conversion import sync as fc_sync
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
        fc.output = base64.b64decode(fc.output)

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
        fc.output = base64.b64decode(fc.output)

    return fc
