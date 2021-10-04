.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: install-dev
install-dev: install
	pip install -r requirements-dev.txt
	python setup.py develop

.PHONY: lint
lint:
	flake8 chaosspring/ tests/
	isort --check-only --profile black chaosspring/ tests/
	black --check --diff chaosspring/ tests/

.PHONY: format
format:
	isort --profile black chaosspring/ tests/
	black chaosspring/ tests/

.PHONY: tests
tests:
	pytest
