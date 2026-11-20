#!/bin/bash
set -e
set -o pipefail

# Remove generated models while preserving the shared model helpers.
for model in kittycad/models/*.py; do
    case "$model" in
        */base.py|*/base64data.py|*/empty.py) ;;
        *) rm "$model" ;;
    esac
done
rm -rf kittycad/api

# Generate new.
uv run python -m generate.generate

# Auto-generate pagination documentation
echo "🔄 Generating pagination documentation..."
uv run python generate/generate_pagination_docs.py

# Format and lint.
uv run ruff check --fix .
uv run ruff format
uv run mypy .
