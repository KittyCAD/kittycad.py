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
poetry run python generate/generate.py

# Format and lint.
poetry run isort .
poetry run black . generate/generate.py docs/conf.py kittycad/client_test.py kittycad/examples_test.py
poetry run ruff check --fix .
poetry run mypy .


# Run the tests.
poetry run pytest kittycad
