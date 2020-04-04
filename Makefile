SERVICE_NAME ?= konduto-sdk
PYTHON_BIN := $(VENV_DIR)/bin
MIN_CODE_COVERAGE ?= 80
PEPS_TO_IGNORE ?= E501
POETRY_VERSION := $(shell poetry --version 2>/dev/null)
DEFAULT_PYTHON_VERSION := 3.8


poetry/setup:
ifdef POETRY_VERSION
	@echo "found poetry version" $(poetry_version)
else
	@echo "poetry not found, we will install the poetry"
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
endif

poetry/env:
	poetry env use $(DEFAULT_PYTHON_VERSION)

poetry/install: poetry/setup poetry/env
	. $$(dirname $$(poetry run which python))/activate; \
	poetry install

setup: poetry/setup
	pip3 install virtualenv
	python3 -m virtualenv $(VENV_DIR)
	$(PYTHON_BIN)/pip3 install pipenv
	$(PYTHON_BIN)/pipenv install

build/code-style:
	pycodestyle --statistics --ignore=$(PEPS_TO_IGNORE) --count konduto/

test/run: build/code-style
	pytest tests --cov=konduto --no-cov-on-fail --cov-fail-under=$(MIN_CODE_COVERAGE)

test: build/code-style test/run

