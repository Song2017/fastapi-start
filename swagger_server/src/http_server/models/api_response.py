# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class ApiResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ApiResponse - a model defined in OpenAPI

        code: The code of this ApiResponse [Optional].
        message: The message of this ApiResponse [Optional].
        sub_message: The sub_message of this ApiResponse [Optional].
        data: The data of this ApiResponse [Optional].
        items: The items of this ApiResponse [Optional].
    """

    code: Optional[int] = Field(alias="code", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    sub_message: Optional[str] = Field(alias="sub_message", default=None)
    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)
    items: Optional[List[object]] = Field(alias="items", default=None)

ApiResponse.update_forward_refs()