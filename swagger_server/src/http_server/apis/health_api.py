# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from http_server.apis.health_api_base import BaseHealthApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from http_server.models.extra_models import TokenModel  # noqa: F401


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/health",
    responses={
        200: {"model": object, "description": "App service health status"},
    },
    tags=["health"],
    summary="health",
    response_model_by_alias=True,
)
async def get_health(
) -> object:
    ...
