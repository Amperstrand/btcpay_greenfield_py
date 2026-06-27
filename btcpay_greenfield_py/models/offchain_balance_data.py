from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OffchainBalanceData")


@_attrs_define
class OffchainBalanceData:
    """
    Attributes:
        opening (None | str | Unset): The amount of current channel openings in millisatoshi
        local (None | str | Unset): The amount that is available on the local end of active channels in millisatoshi
        remote (None | str | Unset): The amount that is available on the remote end of active channels in millisatoshi
        closing (None | str | Unset): The amount of current channel closings in millisatoshi
    """

    opening: None | str | Unset = UNSET
    local: None | str | Unset = UNSET
    remote: None | str | Unset = UNSET
    closing: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        opening: None | str | Unset
        if isinstance(self.opening, Unset):
            opening = UNSET
        else:
            opening = self.opening

        local: None | str | Unset
        if isinstance(self.local, Unset):
            local = UNSET
        else:
            local = self.local

        remote: None | str | Unset
        if isinstance(self.remote, Unset):
            remote = UNSET
        else:
            remote = self.remote

        closing: None | str | Unset
        if isinstance(self.closing, Unset):
            closing = UNSET
        else:
            closing = self.closing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opening is not UNSET:
            field_dict["opening"] = opening
        if local is not UNSET:
            field_dict["local"] = local
        if remote is not UNSET:
            field_dict["remote"] = remote
        if closing is not UNSET:
            field_dict["closing"] = closing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_opening(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening = _parse_opening(d.pop("opening", UNSET))

        def _parse_local(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local = _parse_local(d.pop("local", UNSET))

        def _parse_remote(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote = _parse_remote(d.pop("remote", UNSET))

        def _parse_closing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closing = _parse_closing(d.pop("closing", UNSET))

        offchain_balance_data = cls(
            opening=opening,
            local=local,
            remote=remote,
            closing=closing,
        )

        offchain_balance_data.additional_properties = d
        return offchain_balance_data

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
