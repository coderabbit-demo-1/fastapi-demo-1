# FastAPI Demo 1

A small FastAPI service for demos and integration testing. It provides a health
check and a personalized greeting without a database, authentication, or external
service dependencies. It is a starter example, not a production-ready service.

## Quick start

Use Python 3.12 or newer. From the repository directory:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

On Windows, create the environment with `py -3.12 -m venv .venv`, then activate it
with `.venv\Scripts\Activate.ps1` in PowerShell.

Visit [the interactive API docs](http://127.0.0.1:8000/docs) or inspect the
[OpenAPI schema](http://127.0.0.1:8000/openapi.json). Stop the server with
Ctrl+C.

If you only need to run the service, install `requirements.txt` instead of
`requirements-dev.txt`; the latter also includes the test dependencies.

## API

| Method | Path | Description |
| --- | --- | --- |
| GET | `/` | Returns a welcome message and the docs path. |
| GET | `/health` | Returns `{"status":"ok"}`. |
| POST | `/greet` | Returns a personalized greeting for the supplied name. |

Try the endpoints in another terminal:

```bash
curl http://127.0.0.1:8000/
# {"message":"Hello from FastAPI!","docs":"/docs"}

curl http://127.0.0.1:8000/health
# {"status":"ok"}

curl -X POST http://127.0.0.1:8000/greet \
  -H 'Content-Type: application/json' \
  -d '{"name":"Alex"}'
# {"message":"Hello, Alex!"}
```

`POST /greet` requires a string `name` between 1 and 80 characters. Missing or
invalid values return HTTP 422 with validation details.

## Tests

With the development dependencies installed and the virtual environment active:

```bash
python -m pytest -q
```

The tests cover the endpoints, request validation, OpenAPI schema, and docs route.

## Project layout

- `main.py` — FastAPI application, routes, and request model.
- `test_main.py` — endpoint and validation tests.
- `requirements.in` and `requirements.txt` — runtime dependency inputs and pins.
- `requirements-dev.in` and `requirements-dev.txt` — development dependency
  inputs and pins.
- `.python-version` — the repository's Python version.
