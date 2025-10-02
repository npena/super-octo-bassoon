.PHONY: help install test lint format type-check build clean dev-setup pre-commit-install pre-commit-run docker-build docker-run

# Docker image configuration
IMAGE_NAME ?= super-octo-bassoon
# Derive version from Poetry if available; fallback to 'latest'
VERSION := $(shell poetry version -s 2>/dev/null || echo latest)
DOCKER_TAG_VERSION := $(IMAGE_NAME):$(VERSION)
DOCKER_TAG_LATEST := $(IMAGE_NAME):latest

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	poetry install

dev-setup: install pre-commit-install ## Set up development environment
	@echo "Development environment ready!"

test: ## Run tests
	poetry run pytest

test-cov: ## Run tests with coverage
	poetry run pytest --cov=src --cov-report=html --cov-report=term-missing

lint: ## Run linting
	poetry run flake8 src tests

format: ## Format code
	poetry run black src tests
	poetry run isort src tests

format-check: ## Check code formatting
	poetry run black --check src tests
	poetry run isort --check-only src tests

type-check: ## Run type checking
	poetry run mypy src

pre-commit-install: ## Install pre-commit hooks
	poetry run pre-commit install

pre-commit-run: ## Run pre-commit on all files
	poetry run pre-commit run --all-files

quality: lint format-check type-check ## Run all quality checks

build: ## Build package
	poetry build

clean: ## Clean build artifacts
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

publish: build ## Publish to PyPI (requires authentication)
	poetry publish

version-patch: ## Bump patch version
	poetry version patch

version-minor: ## Bump minor version
	poetry version minor

version-major: ## Bump major version
	poetry version major

release-patch: version-patch ## Create a patch release
	git add pyproject.toml
	git commit -m "Bump version to $$(poetry version -s)"
	git tag "v$$(poetry version -s)"
	@echo "Run 'git push origin main --tags' to trigger release"

release-minor: version-minor ## Create a minor release
	git add pyproject.toml
	git commit -m "Bump version to $$(poetry version -s)"
	git tag "v$$(poetry version -s)"
	@echo "Run 'git push origin main --tags' to trigger release"

release-major: version-major ## Create a major release
	git add pyproject.toml
	git commit -m "Bump version to $$(poetry version -s)"
	git tag "v$$(poetry version -s)"
	@echo "Run 'git push origin main --tags' to trigger release"

docker-build: ## Build multi-stage Docker image (tags: version + latest)
	docker build -t $(DOCKER_TAG_VERSION) -t $(DOCKER_TAG_LATEST) .
	@echo "Built image tags: $(DOCKER_TAG_VERSION), $(DOCKER_TAG_LATEST)"

docker-run: ## Run the Dockerized CLI (pass ARGS="--name Python")
	@if [ -z "$(shell docker images -q $(DOCKER_TAG_VERSION) 2>/dev/null)" ]; then \
	  echo "Image $(DOCKER_TAG_VERSION) not found. Building..."; \
	  $(MAKE) docker-build; \
	fi
	docker run --rm $(DOCKER_TAG_VERSION) $(ARGS)
