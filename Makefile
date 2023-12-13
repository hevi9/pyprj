help::
	echo "Targets:"
	echo "  local"
	echo "  check"
	echo "  clean"
	echo "  build"


local::
	poetry install

local::
	test -d .git && pre-commit install

check::
	poetry run mypy project_name

check::
	poetry run pytest tests

build::
	docker build .
