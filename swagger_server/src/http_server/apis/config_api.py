# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from http_server.apis.config_api_base import BaseConfigApi
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
from http_server.models.api_response import ApiResponse
from http_server.security_api import get_token_ca_key

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/config",
    responses={
        200: {"model": ApiResponse, "description": "Query configuration."},
        400: {"description": "Invalid input."},
        404: {"description": "id check failed."},
        500: {"model": ApiResponse, "description": "id retrieval failed."},
    },
    tags=["config"],
    summary="GetConfig",
    response_model_by_alias=True,
)
async def get_config(
    conf_id: str = Query(None, description="Configuration Id, e.g. sf_express.test"),
    conf_table: str = Query(None, description="Configuration Table, e.g sf_express"),
    token_ca_key: TokenModel = Security(
        get_token_ca_key
    ),
) -> ApiResponse:
    """Get connector config."""
    return BaseConfigApi.subclasses[0]().get_config(conf_id, conf_table)
