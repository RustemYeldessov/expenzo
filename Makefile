insall:
	uv sync

dev-install:
	uv sync --group dev

migrate:
	uv run python3 manage.py migrate

collectstatic:
	uv run python3 manage.py collectstatic --noinput

run:
	uv run python3 manage.py runserver

render-start:
	uv run gunicorn expenzo.wsgi

render-build:
	./build.sh
	uv run python3 manage.py migrate --noinput

build:
	./build.sh

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

test:
	uv run pytest --ds=expenzo.settings --reuse-db

activate:
	source .venv/bin/activate