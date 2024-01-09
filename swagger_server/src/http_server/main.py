# coding: utf-8

"""
    Stem

    This is a demo start for fastAPI

    The version of the OpenAPI document: 0.0.1
    Contact: bensong2017@hotmail.com
    Generated by: https://openapi-generator.tech
"""


from fastapi import FastAPI

from http_server.apis.config_api import router as ConfigApiRouter
from http_server.apis.health_api import router as HealthApiRouter

app = FastAPI(
    title="Stem",
    description="This is a demo start for fastAPI",
    version="0.0.1",
)

app.include_router(ConfigApiRouter)
app.include_router(HealthApiRouter)