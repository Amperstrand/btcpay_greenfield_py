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
from btcpay_greenfield_py.models.payment import Payment
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WebhookInvoiceReceivedPaymentEvent(BaseModel):
    """
    Callback sent if the `type` is `InvoiceReceivedPayment`
    """ # noqa: E501
    delivery_id: Optional[StrictStr] = Field(default=None, description="The delivery id of the webhook", alias="deliveryId")
    webhook_id: Optional[StrictStr] = Field(default=None, description="The id of the webhook", alias="webhookId")
    original_delivery_id: Optional[StrictStr] = Field(default=None, description="If this delivery is a redelivery, the is the delivery id of the original delivery.", alias="originalDeliveryId")
    is_redelivery: Optional[StrictBool] = Field(default=None, description="True if this delivery is a redelivery", alias="isRedelivery")
    type: Optional[StrictStr] = Field(default=None, description="The type of this event, current available are `InvoiceCreated`, `InvoiceReceivedPayment`, `InvoiceProcessing`, `InvoiceExpired`, `InvoiceSettled`, `InvoiceInvalid`, and `InvoicePaymentSettled`.")
    timestamp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A unix timestamp in seconds")
    store_id: Optional[StrictStr] = Field(default=None, description="The store id of the invoice's event", alias="storeId")
    invoice_id: Optional[StrictStr] = Field(default=None, description="The invoice id of the invoice's event", alias="invoiceId")
    metadata: Optional[Union[str, Any]] = Field(default=None, description="User-supplied metadata added to the invoice at the time of its creation")
    after_expiration: Optional[StrictBool] = Field(default=None, description="Whether this payment has been sent after expiration of the invoice", alias="afterExpiration")
    payment_method: Optional[StrictStr] = Field(default=None, description="Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - `\"BTC-OnChain\"` (with the equivalent of `\"BTC\"`)    -`\"BTC-LightningLike\"`: Any supported LN-based payment method (Lightning or LNURL)    - `\"BTC-LightningNetwork\"`: Lightning    - `\"BTC-LNURLPAY\"`: LNURL        Note: Separator can be either `-` or `_`.", alias="paymentMethod")
    payment: Optional[Payment] = None
    __properties: ClassVar[List[str]] = ["deliveryId", "webhookId", "originalDeliveryId", "isRedelivery", "type", "timestamp", "storeId", "invoiceId", "metadata", "afterExpiration", "paymentMethod", "payment"]

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
        """Create an instance of WebhookInvoiceReceivedPaymentEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payment
        if self.payment:
            _dict['payment'] = self.payment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WebhookInvoiceReceivedPaymentEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deliveryId": obj.get("deliveryId"),
            "webhookId": obj.get("webhookId"),
            "originalDeliveryId": obj.get("originalDeliveryId"),
            "isRedelivery": obj.get("isRedelivery"),
            "type": obj.get("type"),
            "timestamp": obj.get("timestamp"),
            "storeId": obj.get("storeId"),
            "invoiceId": obj.get("invoiceId"),
            "metadata": obj.get("metadata"),
            "afterExpiration": obj.get("afterExpiration"),
            "paymentMethod": obj.get("paymentMethod"),
            "payment": Payment.from_dict(obj.get("payment")) if obj.get("payment") is not None else None
        })
        return _obj

