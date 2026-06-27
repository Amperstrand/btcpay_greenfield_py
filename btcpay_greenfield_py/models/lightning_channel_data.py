from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LightningChannelData")


@_attrs_define
class LightningChannelData:
    """
    Attributes:
        remote_node (str | Unset): The public key of the node (Node ID)
        is_public (bool | Unset): Whether the node is public
        is_active (bool | Unset): Whether the node is online
        capacity (str | Unset): The capacity of the channel in millisatoshi
        local_balance (str | Unset): The local balance of the channel in millisatoshi
        channel_point (None | str | Unset):
    """

    remote_node: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    capacity: str | Unset = UNSET
    local_balance: str | Unset = UNSET
    channel_point: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        remote_node = self.remote_node

        is_public = self.is_public

        is_active = self.is_active

        capacity = self.capacity

        local_balance = self.local_balance

        channel_point: None | str | Unset
        if isinstance(self.channel_point, Unset):
            channel_point = UNSET
        else:
            channel_point = self.channel_point

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if remote_node is not UNSET:
            field_dict["remoteNode"] = remote_node
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if local_balance is not UNSET:
            field_dict["localBalance"] = local_balance
        if channel_point is not UNSET:
            field_dict["channelPoint"] = channel_point

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        remote_node = d.pop("remoteNode", UNSET)

        is_public = d.pop("isPublic", UNSET)

        is_active = d.pop("isActive", UNSET)

        capacity = d.pop("capacity", UNSET)

        local_balance = d.pop("localBalance", UNSET)

        def _parse_channel_point(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel_point = _parse_channel_point(d.pop("channelPoint", UNSET))

        lightning_channel_data = cls(
            remote_node=remote_node,
            is_public=is_public,
            is_active=is_active,
            capacity=capacity,
            local_balance=local_balance,
            channel_point=channel_point,
        )

        return lightning_channel_data
