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
poetry run isort --recursive .
poetry run isort generate/generate.py
poetry run black .
poetry run black generate/generate.py
poetry run ruff
