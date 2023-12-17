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
from btcpay_greenfield_py.models.label_data import LabelData
from btcpay_greenfield_py.models.transaction_status import TransactionStatus
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OnChainWalletTransactionData(BaseModel):
    """
    OnChainWalletTransactionData
    """ # noqa: E501
    transaction_hash: Optional[StrictStr] = Field(default=None, description="The transaction id", alias="transactionHash")
    comment: Optional[StrictStr] = Field(default=None, description="A comment linked to the transaction")
    amount: Optional[StrictStr] = Field(default=None, description="The amount the wallet balance changed with this transaction")
    block_hash: Optional[StrictStr] = Field(default=None, description="The hash of the block that confirmed this transaction. Null if still unconfirmed.", alias="blockHash")
    block_height: Optional[StrictStr] = Field(default=None, description="The height of the block that confirmed this transaction. Null if still unconfirmed.", alias="blockHeight")
    confirmations: Optional[StrictStr] = Field(default=None, description="The number of confirmations for this transaction")
    timestamp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A unix timestamp in seconds")
    status: Optional[TransactionStatus] = None
    labels: Optional[List[LabelData]] = Field(default=None, description="Labels linked to this transaction")
    __properties: ClassVar[List[str]] = ["transactionHash", "comment", "amount", "blockHash", "blockHeight", "confirmations", "timestamp", "status", "labels"]

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
        """Create an instance of OnChainWalletTransactionData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        # set to None if transaction_hash (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_hash is None and "transaction_hash" in self.model_fields_set:
            _dict['transactionHash'] = None

        # set to None if block_hash (nullable) is None
        # and model_fields_set contains the field
        if self.block_hash is None and "block_hash" in self.model_fields_set:
            _dict['blockHash'] = None

        # set to None if block_height (nullable) is None
        # and model_fields_set contains the field
        if self.block_height is None and "block_height" in self.model_fields_set:
            _dict['blockHeight'] = None

        # set to None if confirmations (nullable) is None
        # and model_fields_set contains the field
        if self.confirmations is None and "confirmations" in self.model_fields_set:
            _dict['confirmations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OnChainWalletTransactionData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transactionHash": obj.get("transactionHash"),
            "comment": obj.get("comment"),
            "amount": obj.get("amount"),
            "blockHash": obj.get("blockHash"),
            "blockHeight": obj.get("blockHeight"),
            "confirmations": obj.get("confirmations"),
            "timestamp": obj.get("timestamp"),
            "status": obj.get("status"),
            "labels": [LabelData.from_dict(_item) for _item in obj.get("labels")] if obj.get("labels") is not None else None
        })
        return _obj

