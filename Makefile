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
	poetry run mypy X_project_name_X

check::
	poetry run pytest tests

build::
	docker build .
