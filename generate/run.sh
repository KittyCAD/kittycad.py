#!/bin/bash
set -e
set -o pipefail

# Fix for ci.
git config --global --add safe.directory /home/user/src

# Cleanup old stuff.
rm -rf kittycad/models
rm -rf kittycad/api
git checkout kittycad/api/file/create_file_conversion_with_base64_helper.py
git checkout kittycad/api/file/get_file_conversion_with_base64_helper.py

# Generate new.
poetry run python generate/generate.py

# Format and lint.
poetry run isort .
poetry run black .
# We ignore errors here but we should eventually fix them.
poetry run ruff check --fix . || true
# We ignore errors here but we should eventually fix them.
poetry run mypy . || true


# Run the tests.
poetry run pytest kittycad
