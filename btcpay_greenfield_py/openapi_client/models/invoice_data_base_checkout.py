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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from openapi_client.models.object import object
from openapi_client.models.speed_policy import SpeedPolicy
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InvoiceDataBaseCheckout(BaseModel):
    """
    Additional settings to customize the checkout flow
    """ # noqa: E501
    speed_policy: Optional[SpeedPolicy] = Field(default=None, alias="speedPolicy")
    payment_methods: Optional[List[StrictStr]] = Field(default=None, description="A specific set of payment methods to use for this invoice (ie. BTC, BTC-LightningNetwork). By default, select all payment methods enabled in the store.", alias="paymentMethods")
    default_payment_method: Optional[StrictStr] = Field(default=None, description="Payment method IDs are a combination of crypto code and payment type. Available payment method IDs for Bitcoin are:   - `\"BTC-OnChain\"` (with the equivalent of `\"BTC\"`)    -`\"BTC-LightningLike\"`: Any supported LN-based payment method (Lightning or LNURL)    - `\"BTC-LightningNetwork\"`: Lightning    - `\"BTC-LNURLPAY\"`: LNURL        Note: Separator can be either `-` or `_`.", alias="defaultPaymentMethod")
    lazy_payment_methods: Optional[StrictBool] = Field(default=None, description="If true, payment methods are enabled individually upon user interaction in the invoice. Default to store's settings'", alias="lazyPaymentMethods")
    expiration_minutes: Optional[object] = Field(default=None, alias="expirationMinutes")
    monitoring_minutes: Optional[object] = Field(default=None, alias="monitoringMinutes")
    payment_tolerance: Optional[Union[Annotated[float, Field(le=100, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]]] = Field(default=None, description="A percentage determining whether to count the invoice as paid when the invoice is paid within the specified margin of error. Defaults to the store's settings. (The default store settings is 100)", alias="paymentTolerance")
    redirect_url: Optional[StrictStr] = Field(default=None, description="When the customer has paid the invoice, the URL where the customer will be redirected when clicking on the `return to store` button. You can use placeholders `{InvoiceId}` or `{OrderId}` in the URL, BTCPay Server will replace those with this invoice `id` or `metadata.orderId` respectively.", alias="redirectURL")
    redirect_automatically: Optional[StrictBool] = Field(default=None, description="When the customer has paid the invoice, and a `redirectURL` is set, the checkout is redirected to `redirectURL` automatically if `redirectAutomatically` is true. Defaults to the store's settings. (The default store settings is false)", alias="redirectAutomatically")
    requires_refund_email: Optional[StrictBool] = Field(default=None, description="Invoice will require user to provide a refund email if this option is set to `true`. Has no effect if `buyerEmail` metadata is set as there is no email to collect in this case.", alias="requiresRefundEmail")
    checkout_type: Optional[StrictStr] = Field(default=None, description="`\"V1\"`: The original checkout form    `\"V2\"`: The new experimental checkout form.    If `null` or unspecified, the store's settings will be used.", alias="checkoutType")
    default_language: Optional[StrictStr] = Field(default=None, description="The language code (eg. en-US, en, fr-FR...) of the language presented to your customer in the checkout page. BTCPay Server tries to match the best language available. If null or not set, will fallback on the store's default language. You can see the list of language codes with [this operation](#operation/langCodes).", alias="defaultLanguage")
    __properties: ClassVar[List[str]] = ["speedPolicy", "paymentMethods", "defaultPaymentMethod", "lazyPaymentMethods", "expirationMinutes", "monitoringMinutes", "paymentTolerance", "redirectURL", "redirectAutomatically", "requiresRefundEmail", "checkoutType", "defaultLanguage"]

    @field_validator('checkout_type')
    def checkout_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('null', 'V1', 'V2'):
            raise ValueError("must be one of enum values ('null', 'V1', 'V2')")
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
        """Create an instance of InvoiceDataBaseCheckout from a JSON string"""
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
        # set to None if speed_policy (nullable) is None
        # and model_fields_set contains the field
        if self.speed_policy is None and "speed_policy" in self.model_fields_set:
            _dict['speedPolicy'] = None

        # set to None if payment_methods (nullable) is None
        # and model_fields_set contains the field
        if self.payment_methods is None and "payment_methods" in self.model_fields_set:
            _dict['paymentMethods'] = None

        # set to None if default_payment_method (nullable) is None
        # and model_fields_set contains the field
        if self.default_payment_method is None and "default_payment_method" in self.model_fields_set:
            _dict['defaultPaymentMethod'] = None

        # set to None if lazy_payment_methods (nullable) is None
        # and model_fields_set contains the field
        if self.lazy_payment_methods is None and "lazy_payment_methods" in self.model_fields_set:
            _dict['lazyPaymentMethods'] = None

        # set to None if expiration_minutes (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_minutes is None and "expiration_minutes" in self.model_fields_set:
            _dict['expirationMinutes'] = None

        # set to None if monitoring_minutes (nullable) is None
        # and model_fields_set contains the field
        if self.monitoring_minutes is None and "monitoring_minutes" in self.model_fields_set:
            _dict['monitoringMinutes'] = None

        # set to None if payment_tolerance (nullable) is None
        # and model_fields_set contains the field
        if self.payment_tolerance is None and "payment_tolerance" in self.model_fields_set:
            _dict['paymentTolerance'] = None

        # set to None if redirect_url (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_url is None and "redirect_url" in self.model_fields_set:
            _dict['redirectURL'] = None

        # set to None if redirect_automatically (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_automatically is None and "redirect_automatically" in self.model_fields_set:
            _dict['redirectAutomatically'] = None

        # set to None if requires_refund_email (nullable) is None
        # and model_fields_set contains the field
        if self.requires_refund_email is None and "requires_refund_email" in self.model_fields_set:
            _dict['requiresRefundEmail'] = None

        # set to None if checkout_type (nullable) is None
        # and model_fields_set contains the field
        if self.checkout_type is None and "checkout_type" in self.model_fields_set:
            _dict['checkoutType'] = None

        # set to None if default_language (nullable) is None
        # and model_fields_set contains the field
        if self.default_language is None and "default_language" in self.model_fields_set:
            _dict['defaultLanguage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of InvoiceDataBaseCheckout from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "speedPolicy": obj.get("speedPolicy"),
            "paymentMethods": obj.get("paymentMethods"),
            "defaultPaymentMethod": obj.get("defaultPaymentMethod"),
            "lazyPaymentMethods": obj.get("lazyPaymentMethods"),
            "expirationMinutes": obj.get("expirationMinutes"),
            "monitoringMinutes": obj.get("monitoringMinutes"),
            "paymentTolerance": obj.get("paymentTolerance"),
            "redirectURL": obj.get("redirectURL"),
            "redirectAutomatically": obj.get("redirectAutomatically"),
            "requiresRefundEmail": obj.get("requiresRefundEmail"),
            "checkoutType": obj.get("checkoutType"),
            "defaultLanguage": obj.get("defaultLanguage")
        })
        return _obj


