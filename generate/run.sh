#!/bin/bash
set -e
set -o pipefail

# Fix for ci.
git config --global --add safe.directory /home/user/src || true

git add kittycad/models/base64data.py || true
git add kittycad/models/empty.py || true


# Cleanup old stuff.
rm -rf kittycad/models
rm -rf kittycad/api
git checkout kittycad/models/base64data.py || true
git checkout kittycad/models/empty.py || true

# Generate new.
uv run python generate/generate.py

# Format and lint.
uv run ruff check --fix .
uv run ruff format
uv run mypy .


# Run the tests.
uv run pytest kittycad
