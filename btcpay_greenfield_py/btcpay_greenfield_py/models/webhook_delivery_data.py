# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WebhookDeliveryData(BaseModel):
    """
    WebhookDeliveryData
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The id of the delivery")
    timestamp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A unix timestamp in seconds")
    http_code: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="HTTP code received by the remote service, if any.", alias="httpCode")
    error_message: Optional[StrictStr] = Field(default=None, description="User friendly error message, if any.", alias="errorMessage")
    status: Optional[StrictStr] = Field(default=None, description="Whether the delivery failed or not (possible values are: `Failed`, `HttpError`, `HttpSuccess`)")
    __properties: ClassVar[List[str]] = ["id", "timestamp", "httpCode", "errorMessage", "status"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WebhookDeliveryData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if http_code (nullable) is None
        # and model_fields_set contains the field
        if self.http_code is None and "http_code" in self.model_fields_set:
            _dict['httpCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WebhookDeliveryData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "httpCode": obj.get("httpCode"),
            "errorMessage": obj.get("errorMessage"),
            "status": obj.get("status")
        })
        return _obj


