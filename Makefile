all: lint tests

lint:
	flake8 brainmagick && mypy -p brainmagick

tests:
	coverage run -m pytest brainmagick || exit 1
	coverage report --include 'brainmagick/*'

.PHONY: tests lint
