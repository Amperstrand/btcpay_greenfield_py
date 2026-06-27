from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnchainBalanceData")


@_attrs_define
class OnchainBalanceData:
    """
    Attributes:
        confirmed (None | str | Unset): The confirmed amount in satoshi
        unconfirmed (None | str | Unset): The unconfirmed amount in satoshi
        reserved (None | str | Unset): The reserved amount in satoshi
    """

    confirmed: None | str | Unset = UNSET
    unconfirmed: None | str | Unset = UNSET
    reserved: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirmed: None | str | Unset
        if isinstance(self.confirmed, Unset):
            confirmed = UNSET
        else:
            confirmed = self.confirmed

        unconfirmed: None | str | Unset
        if isinstance(self.unconfirmed, Unset):
            unconfirmed = UNSET
        else:
            unconfirmed = self.unconfirmed

        reserved: None | str | Unset
        if isinstance(self.reserved, Unset):
            reserved = UNSET
        else:
            reserved = self.reserved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed
        if unconfirmed is not UNSET:
            field_dict["unconfirmed"] = unconfirmed
        if reserved is not UNSET:
            field_dict["reserved"] = reserved

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_confirmed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmed = _parse_confirmed(d.pop("confirmed", UNSET))

        def _parse_unconfirmed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unconfirmed = _parse_unconfirmed(d.pop("unconfirmed", UNSET))

        def _parse_reserved(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reserved = _parse_reserved(d.pop("reserved", UNSET))

        onchain_balance_data = cls(
            confirmed=confirmed,
            unconfirmed=unconfirmed,
            reserved=reserved,
        )

        onchain_balance_data.additional_properties = d
        return onchain_balance_data

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
