# Get the version from pyproject.toml
VERSION := `uv run python -c "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])"`

# Install dependencies using uv
install:
    uv sync --extra dev

# Generate the api client
generate: install
    ./generate/run.sh

# Run tests
test: install
    uv run pytest kittycad generate/tests

# Run linting and formatting
lint: install
    uv run ruff check --fix .
    uv run ruff format

# Run type checking
typecheck: install
    uv run mypy .

# Generate documentation
docs: install
    rm -rf docs/html docs/_autosummary
    uv run sphinx-build -b html docs/ docs/html/

# Clean generated files
clean:
    rm -rf build/ dist/ *.egg-info/ .coverage htmlcov/
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

# Create a new git tag to prepare to build a release
tag:
    git tag -sa "v{{VERSION}}" -m "v{{VERSION}}"
    @echo "Run git push origin v{{VERSION}} to push your new tag to GitHub and trigger a release."

# Show available commands
help:
    @just --list
