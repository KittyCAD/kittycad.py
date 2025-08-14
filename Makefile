VERSION := $(shell uv run python -c "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])")

.PHONY: install
install: ## Install dependencies using uv.
	uv sync --extra dev

.PHONY: generate
generate: install ## Generate the api client.
	./generate/run.sh

.PHONY: test
test: install ## Run tests.
	uv run pytest kittycad

.PHONY: lint
lint: install ## Run linting and formatting.
	uv run ruff check --fix .
	uv run ruff format
	uv run isort .

.PHONY: typecheck
typecheck: install ## Run type checking.
	uv run mypy .

.PHONY: docs
docs: install ## Generate documentation.
	rm -rf docs/html docs/_autosummary
	uv run sphinx-build -b html docs/ docs/html/

.PHONY: clean
clean: ## Clean generated files.
	rm -rf build/ dist/ *.egg-info/ .coverage htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

.PHONY: tag
tag: ## Create a new git tag to prepare to build a release.
	git tag -sa "v$(VERSION)" -m "v$(VERSION)"
	@echo "Run git push origin v$(VERSION) to push your new tag to GitHub and trigger a release."

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
