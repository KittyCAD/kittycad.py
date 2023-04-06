#!/bin/bash
set -e
set -o pipefail

# This should fix CI.
git config --add safe.directory $(pwd)

# Cleanup old stuff.
rm -rf kittycad/models
rm -rf kittycad/api
git checkout kittycad/api/file/create_file_conversion_with_base64_helper.py
git checkout kittycad/api/file/get_file_conversion_with_base64_helper.py

# Generate new.
poetry run python generate/generate.py
poetry run autopep8 --in-place --aggressive --aggressive kittycad/models/*.py
poetry run autopep8 --in-place --aggressive --aggressive kittycad/api/*.py
poetry run autopep8 --in-place --aggressive --aggressive kittycad/*.py
poetry run autopep8 --in-place --aggressive --aggressive generate/*.py

# Lint
poetry run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
