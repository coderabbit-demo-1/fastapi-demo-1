import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI!", "docs": "/docs"}


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "0.1.0"}


def test_greeting():
    response = client.post("/greet", json={"name": "Alex"})

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alex!"}


def test_greeting_accepts_maximum_name_length():
    name = "A" * 80
    response = client.post("/greet", json={"name": name})

    assert response.status_code == 200
    assert response.json() == {"message": f"Hello, {name}!"}


@pytest.mark.parametrize(
    "payload",
    [
        {"name": ""},
        {},
        {"name": "A" * 81},
        {"name": 123},
    ],
)
def test_greeting_rejects_invalid_name(payload):
    response = client.post("/greet", json=payload)

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "name"]


def test_openapi_schema():
    response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()
    assert schema["info"]["title"] == "FastAPI Demo"
    assert set(schema["paths"]) == {"/", "/health", "/version", "/greet"}
    name_schema = schema["components"]["schemas"]["GreetingRequest"]["properties"]["name"]
    assert name_schema["minLength"] == 1
    assert name_schema["maxLength"] == 80


def test_interactive_docs():
    response = client.get("/docs")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "/openapi.json" in response.text
