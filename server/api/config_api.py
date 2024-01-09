# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

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

from server.api.security_api import get_token_ca_key
from swagger_server.src.http_server.models.api_response import ApiResponse
from swagger_server.src.http_server.models.extra_models import TokenModel

router = APIRouter()


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
    return {"status": "ok"}
