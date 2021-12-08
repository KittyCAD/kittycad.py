# kittycad
A client library for accessing KittyCAD

## Usage
First, create an authenticated client:

```python
from kittycad import AuthenticatedClient

client = AuthenticatedClient(token="your_token")
```

If you want to use the environment variable `KITTYCAD_API_TOKEN` to do
authentication and not pass one to the client, do the following:

```python
from kittycad import AuthenticatedClientFromEnv

client = AuthenticatedClientFromEnv()
```

Now call your endpoint and use your models:

```python
from kittycad.models import AuthSession
from kittycad.api.meta import meta_debug_session
from kittycad.types import Response

session: AuthSession = meta_debug_session.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[AuthSession] = meta_debug_session.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from kittycad.models import AuthSession
from kittycad.api.meta import meta_debug_session
from kittycad.types import Response

session: AuthSession = await meta_debug_session.asyncio(client=client)
response: Response[AuthSession] = await meta_debug_session.asyncio_detailed(client=client)
```
