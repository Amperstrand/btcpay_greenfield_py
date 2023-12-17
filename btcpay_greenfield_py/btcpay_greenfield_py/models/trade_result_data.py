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
from btcpay_greenfield_py.models.ledger_entry_data import LedgerEntryData
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TradeResultData(BaseModel):
    """
    TradeResultData
    """ # noqa: E501
    from_asset: Optional[StrictStr] = Field(default=None, description="The asset to trade.", alias="fromAsset")
    to_asset: Optional[StrictStr] = Field(default=None, description="The asset you want.", alias="toAsset")
    ledger_entries: Optional[List[LedgerEntryData]] = Field(default=None, description="The asset entries that were changed during the trade. This is an array of at least 2 items with the asset sold and the asset gained. It may also include ledger entries for the costs of the trade and possibly exchange tokens used.", alias="ledgerEntries")
    trade_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the trade used by the exchange. This ID can be used to get the details of this trade at a later time.", alias="tradeId")
    account_id: Optional[StrictStr] = Field(default=None, description="The unique ID of the custodian account used.", alias="accountId")
    custodian_code: Optional[StrictStr] = Field(default=None, description="The code of the custodian used.", alias="custodianCode")
    __properties: ClassVar[List[str]] = ["fromAsset", "toAsset", "ledgerEntries", "tradeId", "accountId", "custodianCode"]

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
        """Create an instance of TradeResultData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ledger_entries (list)
        _items = []
        if self.ledger_entries:
            for _item in self.ledger_entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ledgerEntries'] = _items
        # set to None if trade_id (nullable) is None
        # and model_fields_set contains the field
        if self.trade_id is None and "trade_id" in self.model_fields_set:
            _dict['tradeId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TradeResultData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fromAsset": obj.get("fromAsset"),
            "toAsset": obj.get("toAsset"),
            "ledgerEntries": [LedgerEntryData.from_dict(_item) for _item in obj.get("ledgerEntries")] if obj.get("ledgerEntries") is not None else None,
            "tradeId": obj.get("tradeId"),
            "accountId": obj.get("accountId"),
            "custodianCode": obj.get("custodianCode")
        })
        return _obj

