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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PullPaymentsCreatePullPaymentRequest(BaseModel):
    """
    PullPaymentsCreatePullPaymentRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the pull payment")
    description: Optional[StrictStr] = Field(default=None, description="The description of the pull payment")
    amount: Optional[StrictStr] = Field(default=None, description="The amount in `currency` of this pull payment as a decimal string")
    currency: Optional[StrictStr] = Field(default=None, description="The currency of the amount.")
    period: Optional[StrictInt] = Field(default=None, description="The length of each period in seconds.")
    bolt11_expiration: Optional[StrictStr] = Field(default='30', description="If lightning is activated, do not accept BOLT11 invoices with expiration less than … days", alias="BOLT11Expiration")
    auto_approve_claims: Optional[StrictBool] = Field(default=False, description="Any payouts created for this pull payment will skip the approval phase upon creation", alias="autoApproveClaims")
    starts_at: Optional[StrictInt] = Field(default=None, description="When this pull payment is effective. Already started if null or unspecified.", alias="startsAt")
    expires_at: Optional[StrictInt] = Field(default=None, description="When this pull payment expires. Never expires if null or unspecified.", alias="expiresAt")
    payment_methods: Optional[List[StrictStr]] = Field(default=None, description="The list of supported payment methods supported by this pull payment. Available options can be queried from the `StorePaymentMethods_GetStorePaymentMethods` endpoint", alias="paymentMethods")
    __properties: ClassVar[List[str]] = ["name", "description", "amount", "currency", "period", "BOLT11Expiration", "autoApproveClaims", "startsAt", "expiresAt", "paymentMethods"]

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
        """Create an instance of PullPaymentsCreatePullPaymentRequest from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if period (nullable) is None
        # and model_fields_set contains the field
        if self.period is None and "period" in self.model_fields_set:
            _dict['period'] = None

        # set to None if bolt11_expiration (nullable) is None
        # and model_fields_set contains the field
        if self.bolt11_expiration is None and "bolt11_expiration" in self.model_fields_set:
            _dict['BOLT11Expiration'] = None

        # set to None if auto_approve_claims (nullable) is None
        # and model_fields_set contains the field
        if self.auto_approve_claims is None and "auto_approve_claims" in self.model_fields_set:
            _dict['autoApproveClaims'] = None

        # set to None if starts_at (nullable) is None
        # and model_fields_set contains the field
        if self.starts_at is None and "starts_at" in self.model_fields_set:
            _dict['startsAt'] = None

        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expiresAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PullPaymentsCreatePullPaymentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "period": obj.get("period"),
            "BOLT11Expiration": obj.get("BOLT11Expiration") if obj.get("BOLT11Expiration") is not None else '30',
            "autoApproveClaims": obj.get("autoApproveClaims") if obj.get("autoApproveClaims") is not None else False,
            "startsAt": obj.get("startsAt"),
            "expiresAt": obj.get("expiresAt"),
            "paymentMethods": obj.get("paymentMethods")
        })
        return _obj

