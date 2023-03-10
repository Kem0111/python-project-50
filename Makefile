install:
	poetry install

update:
	poetry update

build:
	poetry build 

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

reporter:
	coverage report -m

test-cov:
	poetry run pytest --cov-report xml --cov=gendiff tests/  