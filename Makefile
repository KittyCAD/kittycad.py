DOCKER_IMAGE_NAME := kittycad/python-generator

INTERACTIVE := $(shell [ -t 0 ] && echo 1 || echo 0)
ifeq ($(INTERACTIVE), 1)
	DOCKER_FLAGS += -t
endif

# For this to work, you need to install toml-cli: https://github.com/gnprice/toml-cli
# `cargo install toml-cli`
VERSION := $(shell toml get $(CURDIR)/pyproject.toml tool.poetry.version | jq -r .)

.PHONY: generate
generate: docker-image ## Generate the api client.
	docker run --rm -i $(DOCKER_FLAGS) \
		--name python-generator \
		-v $(CURDIR):/usr/src \
		--workdir /usr/src \
		$(DOCKER_IMAGE_NAME) poetry run python generate/generate.py

.PHONY: shell
shell: docker-image ## Pop into a shell in the docker image.
	docker run --rm -i $(DOCKER_FLAGS) \
		--name python-generator-shell \
		-v $(CURDIR):/usr/src \
		--workdir /usr/src \
		$(DOCKER_IMAGE_NAME) /bin/bash


.PHONY: docker-image
docker-image:
	docker build -t $(DOCKER_IMAGE_NAME) .

.PHONY: tag
tag: ## Create a new git tag to prepare to build a release.
	git tag -sa "v$(VERSION)" -m "v$(VERSION)"
	@echo "Run git push origin v$(VERSION) to push your new tag to GitHub and trigger a release."

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
