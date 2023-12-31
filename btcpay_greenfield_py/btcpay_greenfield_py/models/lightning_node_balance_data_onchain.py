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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LightningNodeBalanceDataOnchain(BaseModel):
    """
    On-chain balance of the Lightning node
    """ # noqa: E501
    confirmed: Optional[StrictStr] = Field(default=None, description="The confirmed amount in satoshi")
    unconfirmed: Optional[StrictStr] = Field(default=None, description="The unconfirmed amount in satoshi")
    reserved: Optional[StrictStr] = Field(default=None, description="The reserved amount in satoshi")
    __properties: ClassVar[List[str]] = ["confirmed", "unconfirmed", "reserved"]

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
        """Create an instance of LightningNodeBalanceDataOnchain from a JSON string"""
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
        # set to None if confirmed (nullable) is None
        # and model_fields_set contains the field
        if self.confirmed is None and "confirmed" in self.model_fields_set:
            _dict['confirmed'] = None

        # set to None if unconfirmed (nullable) is None
        # and model_fields_set contains the field
        if self.unconfirmed is None and "unconfirmed" in self.model_fields_set:
            _dict['unconfirmed'] = None

        # set to None if reserved (nullable) is None
        # and model_fields_set contains the field
        if self.reserved is None and "reserved" in self.model_fields_set:
            _dict['reserved'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LightningNodeBalanceDataOnchain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "confirmed": obj.get("confirmed"),
            "unconfirmed": obj.get("unconfirmed"),
            "reserved": obj.get("reserved")
        })
        return _obj


