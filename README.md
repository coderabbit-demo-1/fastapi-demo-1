# FastAPI Demo 1

A small FastAPI application for demos and integration testing. It provides a
health check and a personalized greeting, with no database, authentication, or
external service dependencies. This is a starter example, not a production-ready
service.

## Quick start

The repository specifies Python 3.12. From the repository root, create a virtual
environment and install the runtime dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

On Windows, use `py -3.12 -m venv .venv` and activate it in PowerShell with
`.venv\Scripts\Activate.ps1` instead of the first two commands above.

Visit <http://127.0.0.1:8000/docs> for interactive API documentation or
<http://127.0.0.1:8000/openapi.json> for the OpenAPI schema. Stop the server
with Ctrl+C.

## API

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/` | Return a welcome message and a link to the docs. |
| GET | `/health` | Return `{"status":"ok"}`. |
| POST | `/greet` | Return a greeting for the supplied name. |

For example:

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

`POST /greet` requires a JSON object with a string `name` between 1 and 80
characters. Invalid requests receive HTTP 422 with validation details.

## Tests

With the virtual environment activated, install the development dependencies
and run the test suite:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The tests cover the endpoints, request validation, OpenAPI schema, and docs route.
