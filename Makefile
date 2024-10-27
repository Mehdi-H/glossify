# This is an auto documented Makefile. For more information see the following article
# @see http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

SHELL := /bin/bash
.SHELLFLAGS = -ec
.SILENT:
MAKEFLAGS += --silent
.ONESHELL:

.EXPORT_ALL_VARIABLES:

.DEFAULT_GOAL: help

.PHONY: help ## 🛟 To display this prompts. This will list all available targets with their documentation
help:
	echo "❓ Use \`make <target>' where <target> is one of 👇"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?##' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'
	echo "Tips 💡"
	echo "	- use tab for auto-completion"
	echo "	- use the dry run option '-n' to show what make is attempting to do. example: environmentName=dev make -n deploy"

.PHONY: dependencies  ## 📦 To install all dependencies
dependencies:
	uv sync

.PHONY: lint  ## 🚨 To run the linter against the codebase
lint:
	uv run ruff check

.PHONY: tests  ## 🧪 To run the tests
tests:
	uv run pytest

.PHONY: glossify  ## 📚 To run the glossify entry point script
glossify:
	uv run python main.py

.PHONY: glossify-help  ## 📚 To display the help message for glossify entry point script
glossify-help:
	uv run python main.py --help