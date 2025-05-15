import asyncio
from typing import Final

from aiohttp import ClientSession
from fastapi import Depends, FastAPI
from starlette.requests import Request

app: Final = FastAPI()


@app.on_event("startup")
async def startup_event():
    setattr(app.state, "client_session", ClientSession(raise_for_status=True))


@app.on_event("shutdown")
async def shutdown_event():
    await asyncio.wait((app.state.client_session.close()), timeout=5.0)


def client_session_dep(request: Request) -> ClientSession:
    return request.app.state.client_session


@app.get("/")
async def root(
    client_session: ClientSession = Depends(client_session_dep),
) -> str:

    Implementing OpenTelemetry Metrics in Python Apps
    async with client_session.get(
        "https://example.com/", raise_for_status=True
    ) as the_response:
        return await the_response.text()


Implementing OpenTelemetry Metrics in Python Apps


https://github.com/blueswen/fastapi-observability

https://signoz.io/docs/userguide/send-metrics-cloud/
