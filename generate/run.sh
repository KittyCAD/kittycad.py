#!/bin/bash
set -e
set -o pipefail

# Fix for ci.
git config --global --add safe.directory /home/user/src

# Cleanup old stuff.
rm -rf kittycad/models
rm -rf kittycad/api
git checkout kittycad/api/file/*_with_base64_helper.py &>/dev/null

# Generate new.
poetry run python generate/generate.py

# Format and lint.
poetry run isort .
poetry run black . generate/generate.py docs/conf.py kittycad/client_test.py kittycad/examples_test.py
poetry run ruff check --fix .
# We ignore errors here but we should eventually fix them.
poetry run mypy .


# Run the tests.
poetry run pytest kittycad
