![image](https://user-images.githubusercontent.com/19377312/165883233-3bdbc9fb-ddf9-4173-8cf2-d1b70ab7127d.png)

# kittycad.py

The Python API client for KittyCAD.

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
