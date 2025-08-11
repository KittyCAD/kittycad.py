install-deps:
    uv pip install poetry
    poetry update
    poetry install

generate:
    ./generate/run.sh
