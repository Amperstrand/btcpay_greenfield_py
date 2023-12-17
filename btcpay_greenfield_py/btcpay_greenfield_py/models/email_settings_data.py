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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EmailSettingsData(BaseModel):
    """
    EmailSettingsData
    """ # noqa: E501
    server: Optional[StrictStr] = Field(default=None, description="Smtp server host")
    port: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Smtp server port")
    login: Optional[StrictStr] = Field(default=None, description="Smtp server username")
    password: Optional[StrictStr] = Field(default=None, description="Smtp server password")
    var_from: Optional[StrictStr] = Field(default=None, description="Email to send from", alias="from")
    from_display: Optional[StrictStr] = Field(default=None, description="The name of the sender", alias="fromDisplay")
    disable_certificate_check: Optional[StrictBool] = Field(default=False, description="Disable TLS certificate security checks", alias="disableCertificateCheck")
    __properties: ClassVar[List[str]] = ["server", "port", "login", "password", "from", "fromDisplay", "disableCertificateCheck"]

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
        """Create an instance of EmailSettingsData from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EmailSettingsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "server": obj.get("server"),
            "port": obj.get("port"),
            "login": obj.get("login"),
            "password": obj.get("password"),
            "from": obj.get("from"),
            "fromDisplay": obj.get("fromDisplay"),
            "disableCertificateCheck": obj.get("disableCertificateCheck") if obj.get("disableCertificateCheck") is not None else False
        })
        return _obj

