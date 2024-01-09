# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from http_server.models.api_response import ApiResponse
from http_server.security_api import get_token_ca_key

class BaseConfigApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseConfigApi.subclasses = BaseConfigApi.subclasses + (cls,)
    def get_config(
        self,
        conf_id: str,
        conf_table: str,
    ) -> ApiResponse:
        """Get connector config."""
        ...
