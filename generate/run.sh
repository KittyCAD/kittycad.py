#!/bin/bash
set -e
set -o pipefail

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
