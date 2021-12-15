from typing import Any, Dict, Optional, Union

import base64
import httpx

from ...client import AuthenticatedClient
from ...models.file_conversion import FileConversion
from ...types import Response
from ...api.file.file_conversion_by_id import sync as fc_sync, asyncio as fc_asyncio


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, FileConversion]]:
    """Get the status of a file conversion. This function automatically base64 decodes the output response if there is one."""

    fc = fc_sync(
        id=id,
        client=client,
    )

    if fc.output != "":
        fc.output = base64.b64decode(fc.output)

    return fc


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, FileConversion]]:
    """Get the status of a file conversion. This function automatically base64 decodes the output response if there is one."""

    fc = await fc_asyncio(
            id=id,
            client=client,
        )

    if fc.output != "":
        fc.output = base64.b64decode(fc.output)

    return fc
