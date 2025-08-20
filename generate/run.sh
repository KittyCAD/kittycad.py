#!/bin/bash
set -e
set -o pipefail

git add kittycad/models/base64data.py || true
git add kittycad/models/empty.py || true


# Cleanup old stuff.
rm -rf kittycad/models
rm -rf kittycad/api
git checkout kittycad/models/base64data.py || true
git checkout kittycad/models/empty.py || true
git checkout kittycad/models/base.py || true

# Generate new.
uv run python -m generate.generate

# Auto-generate pagination documentation
echo "🔄 Generating pagination documentation..."
uv run python generate/generate_pagination_docs.py

# Format and lint.
uv run ruff check --fix .
uv run ruff format
uv run mypy .
