.PHONY: help install fmt lint test build publish clean

.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies in a virtual env
	poetry install

fmt: ## Format code with black and isort
	poetry run isort src tests
	poetry run black src tests

lint: ## Lint with flake8
	poetry run flake8 src tests

test: ## Run pytest
	poetry run pytest --maxfail=1 --disable-warnings -q

build: ## Build wheel and sdist
	poetry build

publish: ## Publish to PyPI
	poetry publish --build

clean: ## Clean build artifacts
	rm -rf build dist *.egg-info
