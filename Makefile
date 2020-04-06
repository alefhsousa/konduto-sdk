SERVICE_NAME ?= konduto-sdk
POETRY_BIN := $(HOME)/.poetry/bin
MIN_CODE_COVERAGE ?= 80
PEPS_TO_IGNORE ?= E501
POETRY_VERSION := $(shell poetry --version 2>/dev/null)
DEFAULT_PYTHON_VERSION ?= 3.8


poetry/setup:
ifdef POETRY_VERSION
	@echo "found poetry version" $(poetry_version)
else
	@echo "poetry not found, we will install the poetry"
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
endif

poetry/env:
	$(POETRY_BIN)/poetry env use $(DEFAULT_PYTHON_VERSION)

poetry/install: poetry/setup poetry/env
	. $$(dirname $$($(POETRY_BIN)/poetry run which python))/activate; \
	$(POETRY_BIN)/poetry install

build/code-style:
	. $$(dirname $$($(POETRY_BIN)/poetry run which python))/activate; \
	pycodestyle --statistics --ignore=$(PEPS_TO_IGNORE) --count konduto/

test/run:
	. $$(dirname $$($(POETRY_BIN)/poetry run which python))/activate; \
	pytest tests --cov=konduto --cov-report=term --cov-report=xml --no-cov-on-fail --cov-fail-under=$(MIN_CODE_COVERAGE)

test: test/run

setup: poetry/install

build: poetry/install
	. $$(dirname $$($(POETRY_BIN)/poetry run which python))/activate; \
	$(POETRY_BIN)/poetry build; \
	ls -lrth dist/

