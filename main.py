"""A small FastAPI app for demos and integration testing."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="FastAPI Demo",
    description="A tiny API with a health check and a personalized greeting.",
    version="0.1.0",
)


class GreetingRequest(BaseModel):
    name: str = Field(min_length=1, max_length=80)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!", "docs": "/docs"}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/version")
async def version() -> dict[str, str]:
    return {"version": app.version}


@app.post("/greet")
async def greet(request: GreetingRequest) -> dict[str, str]:
    return {"message": f"Hello, {request.name}!"}
