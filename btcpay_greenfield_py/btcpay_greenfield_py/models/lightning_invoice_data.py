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
from btcpay_greenfield_py.models.lightning_invoice_status import LightningInvoiceStatus
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LightningInvoiceData(BaseModel):
    """
    LightningInvoiceData
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The invoice's ID")
    status: Optional[LightningInvoiceStatus] = None
    bolt11: Optional[StrictStr] = Field(default=None, description="The BOLT11 representation of the invoice", alias="BOLT11")
    paid_at: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A unix timestamp in seconds", alias="paidAt")
    expires_at: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A unix timestamp in seconds", alias="expiresAt")
    amount: Optional[StrictStr] = Field(default=None, description="The amount of the invoice in millisatoshi")
    amount_received: Optional[StrictStr] = Field(default=None, description="The amount received in millisatoshi", alias="amountReceived")
    payment_hash: Optional[StrictStr] = Field(default=None, description="The payment hash", alias="paymentHash")
    preimage: Optional[StrictStr] = Field(default=None, description="The payment preimage (available when status is complete)")
    custom_records: Optional[Union[str, Any]] = Field(default=None, description="The custom TLV records attached to a keysend payment", alias="customRecords")
    __properties: ClassVar[List[str]] = ["id", "status", "BOLT11", "paidAt", "expiresAt", "amount", "amountReceived", "paymentHash", "preimage", "customRecords"]

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
        """Create an instance of LightningInvoiceData from a JSON string"""
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
        # set to None if paid_at (nullable) is None
        # and model_fields_set contains the field
        if self.paid_at is None and "paid_at" in self.model_fields_set:
            _dict['paidAt'] = None

        # set to None if preimage (nullable) is None
        # and model_fields_set contains the field
        if self.preimage is None and "preimage" in self.model_fields_set:
            _dict['preimage'] = None

        # set to None if custom_records (nullable) is None
        # and model_fields_set contains the field
        if self.custom_records is None and "custom_records" in self.model_fields_set:
            _dict['customRecords'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LightningInvoiceData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "BOLT11": obj.get("BOLT11"),
            "paidAt": obj.get("paidAt"),
            "expiresAt": obj.get("expiresAt"),
            "amount": obj.get("amount"),
            "amountReceived": obj.get("amountReceived"),
            "paymentHash": obj.get("paymentHash"),
            "preimage": obj.get("preimage"),
            "customRecords": obj.get("customRecords")
        })
        return _obj


