from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerEntryData")


@_attrs_define
class LedgerEntryData:
    """A single ledger entry meaning an asset and qty has changed (increased or decreased).

    Example:
        {'asset': 'BTC', 'qty': '1.23456', 'type': 'Trade'}

    Attributes:
        asset (str | Unset): An asset.
        qty (str | Unset): The quantity changed of the asset. Can be positive or negative.
        type_ (str | Unset): Trade, Fee or Withdrawal
    """

    asset: str | Unset = UNSET
    qty: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset = self.asset

        qty = self.qty

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset is not UNSET:
            field_dict["asset"] = asset
        if qty is not UNSET:
            field_dict["qty"] = qty
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset = d.pop("asset", UNSET)

        qty = d.pop("qty", UNSET)

        type_ = d.pop("type", UNSET)

        ledger_entry_data = cls(
            asset=asset,
            qty=qty,
            type_=type_,
        )

        ledger_entry_data.additional_properties = d
        return ledger_entry_data

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
