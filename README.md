# FastAPI Demo 1

A small Python API for demos and integration testing. It has no database,
authentication, or external service dependencies. It is a starter example, not a
production-ready service.

## Run locally

Use Python 3.12 or newer. From the repository directory:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Open the interactive API docs at <http://127.0.0.1:8000/docs> or the OpenAPI schema
at <http://127.0.0.1:8000/openapi.json>.

On Windows, create the environment with `py -3.12 -m venv .venv`, then activate it
with `.venv\Scripts\Activate.ps1` in PowerShell instead of
`source .venv/bin/activate`.

## Try the API

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

The `/health` endpoint returns a static response and does not check external
dependencies.

`POST /greet` requires a string `name` between 1 and 80 characters. Invalid
requests receive HTTP 422 with validation details.

## Run tests

With the virtual environment activated:

```bash
python -m pytest -q
```

The tests cover the endpoints, request validation, OpenAPI schema, and docs route.
Only runtime dependencies are needed to run the app; install them with
`python -m pip install -r requirements.txt` if you do not need the test tools.
