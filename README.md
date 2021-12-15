# kittycad.py

The Python API client for KittyCAD.

This is generated from
[openapi-generators/openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

- [PyPI](https://pypi.org/project/kittycad/)
- [Python docs](https://python.api.docs.kittycad.io/)
- [KittyCAD API Docs](https://docs.kittycad.io/?lang=python)

## Generating

You can trigger a build with the GitHub action to generate the client. This will
automatically update the client to the latest version based on the spec hosted
at [api.kittycad.io](https://api.kittycad.io/).

Alternatively, if you wish to generate the client locally, make sure you have
[Docker installed](https://docs.docker.com/get-docker/) and run:

```bash
$ make generate
```

## Contributing

Please do not change the code directly since it is generated. PRs that change
the code directly will be automatically closed by a bot.

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
