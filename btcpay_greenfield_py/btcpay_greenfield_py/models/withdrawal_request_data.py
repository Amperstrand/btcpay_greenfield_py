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
from btcpay_greenfield_py.models.withdrawal_request_data_qty import WithdrawalRequestDataQty
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WithdrawalRequestData(BaseModel):
    """
    WithdrawalRequestData
    """ # noqa: E501
    payment_method: Optional[StrictStr] = Field(default=None, description="Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - `\"BTC-OnChain\"` (with the equivalent of `\"BTC\"`)    -`\"BTC-LightningLike\"`: Any supported LN-based payment method (Lightning or LNURL)    - `\"BTC-LightningNetwork\"`: Lightning    - `\"BTC-LNURLPAY\"`: LNURL        Note: Separator can be either `-` or `_`.", alias="paymentMethod")
    qty: Optional[WithdrawalRequestDataQty] = None
    __properties: ClassVar[List[str]] = ["paymentMethod", "qty"]

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
        """Create an instance of WithdrawalRequestData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of qty
        if self.qty:
            _dict['qty'] = self.qty.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WithdrawalRequestData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "paymentMethod": obj.get("paymentMethod"),
            "qty": WithdrawalRequestDataQty.from_dict(obj.get("qty")) if obj.get("qty") is not None else None
        })
        return _obj

