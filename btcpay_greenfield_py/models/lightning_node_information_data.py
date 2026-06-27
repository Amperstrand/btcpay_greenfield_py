from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LightningNodeInformationData")


@_attrs_define
class LightningNodeInformationData:
    """
    Attributes:
        node_ur_is (list[str] | Unset): Node URIs to connect to this node in the form `pubkey@endpoint[:port]`
        block_height (int | Unset): The block height of the lightning node
        alias (None | str | Unset): The alias of the lightning node
        color (None | str | Unset): The color attribute of the lightning node
        version (None | str | Unset): The version name of the lightning node
        peers_count (int | None | Unset): The number of peers
        active_channels_count (int | None | Unset): The number of active channels
        inactive_channels_count (int | None | Unset): The number of inactive channels
        pending_channels_count (int | None | Unset): The number of pending channels
    """

    node_ur_is: list[str] | Unset = UNSET
    block_height: int | Unset = UNSET
    alias: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    peers_count: int | None | Unset = UNSET
    active_channels_count: int | None | Unset = UNSET
    inactive_channels_count: int | None | Unset = UNSET
    pending_channels_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_ur_is: list[str] | Unset = UNSET
        if not isinstance(self.node_ur_is, Unset):
            node_ur_is = self.node_ur_is

        block_height = self.block_height

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        peers_count: int | None | Unset
        if isinstance(self.peers_count, Unset):
            peers_count = UNSET
        else:
            peers_count = self.peers_count

        active_channels_count: int | None | Unset
        if isinstance(self.active_channels_count, Unset):
            active_channels_count = UNSET
        else:
            active_channels_count = self.active_channels_count

        inactive_channels_count: int | None | Unset
        if isinstance(self.inactive_channels_count, Unset):
            inactive_channels_count = UNSET
        else:
            inactive_channels_count = self.inactive_channels_count

        pending_channels_count: int | None | Unset
        if isinstance(self.pending_channels_count, Unset):
            pending_channels_count = UNSET
        else:
            pending_channels_count = self.pending_channels_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_ur_is is not UNSET:
            field_dict["nodeURIs"] = node_ur_is
        if block_height is not UNSET:
            field_dict["blockHeight"] = block_height
        if alias is not UNSET:
            field_dict["alias"] = alias
        if color is not UNSET:
            field_dict["color"] = color
        if version is not UNSET:
            field_dict["version"] = version
        if peers_count is not UNSET:
            field_dict["peersCount"] = peers_count
        if active_channels_count is not UNSET:
            field_dict["activeChannelsCount"] = active_channels_count
        if inactive_channels_count is not UNSET:
            field_dict["inactiveChannelsCount"] = inactive_channels_count
        if pending_channels_count is not UNSET:
            field_dict["pendingChannelsCount"] = pending_channels_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_ur_is = cast(list[str], d.pop("nodeURIs", UNSET))

        block_height = d.pop("blockHeight", UNSET)

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_peers_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        peers_count = _parse_peers_count(d.pop("peersCount", UNSET))

        def _parse_active_channels_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        active_channels_count = _parse_active_channels_count(d.pop("activeChannelsCount", UNSET))

        def _parse_inactive_channels_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        inactive_channels_count = _parse_inactive_channels_count(d.pop("inactiveChannelsCount", UNSET))

        def _parse_pending_channels_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pending_channels_count = _parse_pending_channels_count(d.pop("pendingChannelsCount", UNSET))

        lightning_node_information_data = cls(
            node_ur_is=node_ur_is,
            block_height=block_height,
            alias=alias,
            color=color,
            version=version,
            peers_count=peers_count,
            active_channels_count=active_channels_count,
            inactive_channels_count=inactive_channels_count,
            pending_channels_count=pending_channels_count,
        )

        lightning_node_information_data.additional_properties = d
        return lightning_node_information_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
