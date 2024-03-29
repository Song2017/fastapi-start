# coding: utf-8

from typing import Dict, List  # noqa: F401

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

router = APIRouter()


@router.get(
    "/health",
    responses={
        200: {"model": str, "description": "BBC order service health status"},
    },
    tags=["health"],
    summary="health",
)
async def get_health(
) -> object:
    return {"status": "ok"}
