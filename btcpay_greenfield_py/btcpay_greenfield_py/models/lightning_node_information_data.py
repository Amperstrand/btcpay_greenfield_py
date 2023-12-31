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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LightningNodeInformationData(BaseModel):
    """
    LightningNodeInformationData
    """ # noqa: E501
    node_uris: Optional[List[StrictStr]] = Field(default=None, description="Node URIs to connect to this node in the form `pubkey@endpoint[:port]`", alias="nodeURIs")
    block_height: Optional[StrictInt] = Field(default=None, description="The block height of the lightning node", alias="blockHeight")
    alias: Optional[StrictStr] = Field(default=None, description="The alias of the lightning node")
    color: Optional[StrictStr] = Field(default=None, description="The color attribute of the lightning node")
    version: Optional[StrictStr] = Field(default=None, description="The version name of the lightning node")
    peers_count: Optional[StrictInt] = Field(default=None, description="The number of peers", alias="peersCount")
    active_channels_count: Optional[StrictInt] = Field(default=None, description="The number of active channels", alias="activeChannelsCount")
    inactive_channels_count: Optional[StrictInt] = Field(default=None, description="The number of inactive channels", alias="inactiveChannelsCount")
    pending_channels_count: Optional[StrictInt] = Field(default=None, description="The number of pending channels", alias="pendingChannelsCount")
    __properties: ClassVar[List[str]] = ["nodeURIs", "blockHeight", "alias", "color", "version", "peersCount", "activeChannelsCount", "inactiveChannelsCount", "pendingChannelsCount"]

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
        """Create an instance of LightningNodeInformationData from a JSON string"""
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
        # set to None if alias (nullable) is None
        # and model_fields_set contains the field
        if self.alias is None and "alias" in self.model_fields_set:
            _dict['alias'] = None

        # set to None if color (nullable) is None
        # and model_fields_set contains the field
        if self.color is None and "color" in self.model_fields_set:
            _dict['color'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if peers_count (nullable) is None
        # and model_fields_set contains the field
        if self.peers_count is None and "peers_count" in self.model_fields_set:
            _dict['peersCount'] = None

        # set to None if active_channels_count (nullable) is None
        # and model_fields_set contains the field
        if self.active_channels_count is None and "active_channels_count" in self.model_fields_set:
            _dict['activeChannelsCount'] = None

        # set to None if inactive_channels_count (nullable) is None
        # and model_fields_set contains the field
        if self.inactive_channels_count is None and "inactive_channels_count" in self.model_fields_set:
            _dict['inactiveChannelsCount'] = None

        # set to None if pending_channels_count (nullable) is None
        # and model_fields_set contains the field
        if self.pending_channels_count is None and "pending_channels_count" in self.model_fields_set:
            _dict['pendingChannelsCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LightningNodeInformationData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodeURIs": obj.get("nodeURIs"),
            "blockHeight": obj.get("blockHeight"),
            "alias": obj.get("alias"),
            "color": obj.get("color"),
            "version": obj.get("version"),
            "peersCount": obj.get("peersCount"),
            "activeChannelsCount": obj.get("activeChannelsCount"),
            "inactiveChannelsCount": obj.get("inactiveChannelsCount"),
            "pendingChannelsCount": obj.get("pendingChannelsCount")
        })
        return _obj


