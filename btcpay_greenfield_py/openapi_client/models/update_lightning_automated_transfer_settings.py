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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateLightningAutomatedTransferSettings(BaseModel):
    """
    UpdateLightningAutomatedTransferSettings
    """ # noqa: E501
    interval_seconds: Optional[object] = Field(default=None, alias="intervalSeconds")
    cancel_payout_after_failures: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many failures should the processor tolerate before cancelling the payout", alias="cancelPayoutAfterFailures")
    process_new_payouts_instantly: Optional[StrictBool] = Field(default=False, description="Skip the interval when ane eligible payout has been approved (or created with pre-approval)", alias="processNewPayoutsInstantly")
    __properties: ClassVar[List[str]] = ["intervalSeconds", "cancelPayoutAfterFailures", "processNewPayoutsInstantly"]

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
        """Create an instance of UpdateLightningAutomatedTransferSettings from a JSON string"""
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
        # set to None if cancel_payout_after_failures (nullable) is None
        # and model_fields_set contains the field
        if self.cancel_payout_after_failures is None and "cancel_payout_after_failures" in self.model_fields_set:
            _dict['cancelPayoutAfterFailures'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateLightningAutomatedTransferSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "intervalSeconds": obj.get("intervalSeconds"),
            "cancelPayoutAfterFailures": obj.get("cancelPayoutAfterFailures"),
            "processNewPayoutsInstantly": obj.get("processNewPayoutsInstantly") if obj.get("processNewPayoutsInstantly") is not None else False
        })
        return _obj


