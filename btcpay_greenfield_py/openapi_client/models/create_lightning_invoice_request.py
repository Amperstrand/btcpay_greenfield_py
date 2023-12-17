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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateLightningInvoiceRequest(BaseModel):
    """
    CreateLightningInvoiceRequest
    """ # noqa: E501
    amount: Optional[StrictStr] = Field(default=None, description="Amount wrapped in a string, represented in a millistatoshi string. (1000 millisatoshi = 1 satoshi)")
    description: Optional[StrictStr] = Field(default=None, description="Description of the invoice in the BOLT11")
    description_hash_only: Optional[StrictBool] = Field(default=False, description="If `descriptionHashOnly` is `true` (default is `false`), then the BOLT11 returned contains a hash of the `description`, rather than the `description`, itself. This allows for much longer descriptions, but they must be communicated via some other mechanism.", alias="descriptionHashOnly")
    expiry: Optional[object] = None
    private_route_hints: Optional[StrictBool] = Field(default=False, description="True if the invoice should include private route hints", alias="privateRouteHints")
    __properties: ClassVar[List[str]] = ["amount", "description", "descriptionHashOnly", "expiry", "privateRouteHints"]

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
        """Create an instance of CreateLightningInvoiceRequest from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if description_hash_only (nullable) is None
        # and model_fields_set contains the field
        if self.description_hash_only is None and "description_hash_only" in self.model_fields_set:
            _dict['descriptionHashOnly'] = None

        # set to None if private_route_hints (nullable) is None
        # and model_fields_set contains the field
        if self.private_route_hints is None and "private_route_hints" in self.model_fields_set:
            _dict['privateRouteHints'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateLightningInvoiceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "description": obj.get("description"),
            "descriptionHashOnly": obj.get("descriptionHashOnly") if obj.get("descriptionHashOnly") is not None else False,
            "expiry": obj.get("expiry"),
            "privateRouteHints": obj.get("privateRouteHints") if obj.get("privateRouteHints") is not None else False
        })
        return _obj


