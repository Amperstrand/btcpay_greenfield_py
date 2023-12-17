# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from pydantic import Field
from btcpay_greenfield_py.models.invoice_payment_method_data_model_additional_data_any_of import InvoicePaymentMethodDataModelAdditionalDataAnyOf
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

INVOICEPAYMENTMETHODDATAMODELADDITIONALDATA_ANY_OF_SCHEMAS = ["InvoicePaymentMethodDataModelAdditionalDataAnyOf", "object"]

class InvoicePaymentMethodDataModelAdditionalData(BaseModel):
    """
    Additional data provided by the payment method.
    """

    # data type: InvoicePaymentMethodDataModelAdditionalDataAnyOf
    anyof_schema_1_validator: Optional[InvoicePaymentMethodDataModelAdditionalDataAnyOf] = None
    # data type: object
    anyof_schema_2_validator: Optional[Union[str, Any]] = Field(default=None, description="No additional information")
    if TYPE_CHECKING:
        actual_instance: Optional[Union[InvoicePaymentMethodDataModelAdditionalDataAnyOf, object]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Literal[INVOICEPAYMENTMETHODDATAMODELADDITIONALDATA_ANY_OF_SCHEMAS]

    model_config = {
        "validate_assignment": True
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = InvoicePaymentMethodDataModelAdditionalData.model_construct()
        error_messages = []
        # validate data type: InvoicePaymentMethodDataModelAdditionalDataAnyOf
        if not isinstance(v, InvoicePaymentMethodDataModelAdditionalDataAnyOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InvoicePaymentMethodDataModelAdditionalDataAnyOf`")
        else:
            return v

        # validate data type: object
        try:
            instance.anyof_schema_2_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in InvoicePaymentMethodDataModelAdditionalData with anyOf schemas: InvoicePaymentMethodDataModelAdditionalDataAnyOf, object. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[InvoicePaymentMethodDataModelAdditionalDataAnyOf] = None
        try:
            instance.actual_instance = InvoicePaymentMethodDataModelAdditionalDataAnyOf.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # deserialize data into object
        try:
            # validation
            instance.anyof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_2_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into InvoicePaymentMethodDataModelAdditionalData with anyOf schemas: InvoicePaymentMethodDataModelAdditionalDataAnyOf, object. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

