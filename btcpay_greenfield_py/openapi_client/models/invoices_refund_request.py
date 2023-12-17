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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InvoicesRefundRequest(BaseModel):
    """
    InvoicesRefundRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Name of the pull payment (Default: 'Refund' followed by the invoice id)")
    description: Optional[StrictStr] = Field(default=None, description="Description of the pull payment")
    payment_method: Optional[StrictStr] = Field(default=None, description="Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - `\"BTC-OnChain\"` (with the equivalent of `\"BTC\"`)    -`\"BTC-LightningLike\"`: Any supported LN-based payment method (Lightning or LNURL)    - `\"BTC-LightningNetwork\"`: Lightning    - `\"BTC-LNURLPAY\"`: LNURL        Note: Separator can be either `-` or `_`.", alias="paymentMethod")
    refund_variant: Optional[StrictStr] = Field(default=None, description="* `RateThen`: Refund the crypto currency price, at the rate the invoice got paid.  * `CurrentRate`: Refund the crypto currency price, at the current rate.  *`Fiat`: Refund the invoice currency, at the rate when the refund will be sent.  *`OverpaidAmount`: Refund the crypto currency amount that was overpaid.  *`Custom`: Specify the amount, currency, and rate of the refund. (see `customAmount` and `customCurrency`)", alias="refundVariant")
    subtract_percentage: Optional[StrictStr] = Field(default=None, description="Optional percentage by which to reduce the refund, e.g. as processing charge or to compensate for the mining fee.", alias="subtractPercentage")
    custom_amount: Optional[StrictStr] = Field(default=None, description="The amount to refund if the `refundVariant` is `Custom`.", alias="customAmount")
    custom_currency: Optional[StrictStr] = Field(default=None, description="The currency to refund if the `refundVariant` is `Custom`", alias="customCurrency")
    __properties: ClassVar[List[str]] = ["name", "description", "paymentMethod", "refundVariant", "subtractPercentage", "customAmount", "customCurrency"]

    @field_validator('refund_variant')
    def refund_variant_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CurrentRate', 'Custom', 'Fiat', 'OverpaidAmount', 'RateThen'):
            raise ValueError("must be one of enum values ('CurrentRate', 'Custom', 'Fiat', 'OverpaidAmount', 'RateThen')")
        return value

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
        """Create an instance of InvoicesRefundRequest from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of InvoicesRefundRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "paymentMethod": obj.get("paymentMethod"),
            "refundVariant": obj.get("refundVariant"),
            "subtractPercentage": obj.get("subtractPercentage"),
            "customAmount": obj.get("customAmount"),
            "customCurrency": obj.get("customCurrency")
        })
        return _obj


