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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PaymentRequestData(BaseModel):
    """
    PaymentRequestData
    """ # noqa: E501
    amount: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The amount of the payment request")
    title: Optional[StrictStr] = Field(default=None, description="The title of the payment request")
    currency: Optional[StrictStr] = Field(default=None, description="The currency of the payment request. If empty, the store's default currency code will be used.")
    email: Optional[StrictStr] = Field(default=None, description="The email used in invoices generated by the payment request")
    description: Optional[StrictStr] = Field(default=None, description="The description of the payment request")
    expiry_date: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A unix timestamp in seconds", alias="expiryDate")
    embedded_css: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Custom CSS styling for the payment request", alias="embeddedCSS")
    custom_css_link: Optional[StrictStr] = Field(default=None, description="Custom CSS link for styling the payment request", alias="customCSSLink")
    allow_custom_payment_amounts: Optional[StrictBool] = Field(default=None, description="Whether to allow users to create invoices that partially pay the payment request ", alias="allowCustomPaymentAmounts")
    form_id: Optional[StrictStr] = Field(default=None, description="Form ID to request customer data", alias="formId")
    form_response: Optional[Union[str, Any]] = Field(default=None, description="Form data response", alias="formResponse")
    id: Optional[StrictStr] = Field(default=None, description="The id of the payment request")
    store_id: Optional[StrictStr] = Field(default=None, description="The store identifier that the payment request belongs to", alias="storeId")
    status: Optional[StrictStr] = Field(default=None, description="The status of the payment request")
    created_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A unix timestamp in seconds", alias="createdTime")
    __properties: ClassVar[List[str]] = ["amount", "title", "currency", "email", "description", "expiryDate", "embeddedCSS", "customCSSLink", "allowCustomPaymentAmounts", "formId", "formResponse", "id", "storeId", "status", "createdTime"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Pending', 'Completed', 'Expired'):
            raise ValueError("must be one of enum values ('Pending', 'Completed', 'Expired')")
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
        """Create an instance of PaymentRequestData from a JSON string"""
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
        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if expiry_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_date is None and "expiry_date" in self.model_fields_set:
            _dict['expiryDate'] = None

        # set to None if embedded_css (nullable) is None
        # and model_fields_set contains the field
        if self.embedded_css is None and "embedded_css" in self.model_fields_set:
            _dict['embeddedCSS'] = None

        # set to None if custom_css_link (nullable) is None
        # and model_fields_set contains the field
        if self.custom_css_link is None and "custom_css_link" in self.model_fields_set:
            _dict['customCSSLink'] = None

        # set to None if allow_custom_payment_amounts (nullable) is None
        # and model_fields_set contains the field
        if self.allow_custom_payment_amounts is None and "allow_custom_payment_amounts" in self.model_fields_set:
            _dict['allowCustomPaymentAmounts'] = None

        # set to None if form_id (nullable) is None
        # and model_fields_set contains the field
        if self.form_id is None and "form_id" in self.model_fields_set:
            _dict['formId'] = None

        # set to None if form_response (nullable) is None
        # and model_fields_set contains the field
        if self.form_response is None and "form_response" in self.model_fields_set:
            _dict['formResponse'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PaymentRequestData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "title": obj.get("title"),
            "currency": obj.get("currency"),
            "email": obj.get("email"),
            "description": obj.get("description"),
            "expiryDate": obj.get("expiryDate"),
            "embeddedCSS": obj.get("embeddedCSS"),
            "customCSSLink": obj.get("customCSSLink"),
            "allowCustomPaymentAmounts": obj.get("allowCustomPaymentAmounts"),
            "formId": obj.get("formId"),
            "formResponse": obj.get("formResponse"),
            "id": obj.get("id"),
            "storeId": obj.get("storeId"),
            "status": obj.get("status"),
            "createdTime": obj.get("createdTime")
        })
        return _obj


