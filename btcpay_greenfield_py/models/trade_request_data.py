from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TradeRequestData")


@_attrs_define
class TradeRequestData:
    """
    Example:
        {'fromAsset': 'USD', 'toAsset': 'BTC', 'qty': '50%'}

    Attributes:
        from_asset (str | Unset): The asset to trade.
        to_asset (str | Unset): The asset you want.
        qty (str | Unset):
    """

    from_asset: str | Unset = UNSET
    to_asset: str | Unset = UNSET
    qty: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_asset = self.from_asset

        to_asset = self.to_asset

        qty: str | Unset
        if isinstance(self.qty, Unset):
            qty = UNSET
        else:
            qty = self.qty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_asset is not UNSET:
            field_dict["fromAsset"] = from_asset
        if to_asset is not UNSET:
            field_dict["toAsset"] = to_asset
        if qty is not UNSET:
            field_dict["qty"] = qty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_asset = d.pop("fromAsset", UNSET)

        to_asset = d.pop("toAsset", UNSET)

        def _parse_qty(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        qty = _parse_qty(d.pop("qty", UNSET))

        trade_request_data = cls(
            from_asset=from_asset,
            to_asset=to_asset,
            qty=qty,
        )

        trade_request_data.additional_properties = d
        return trade_request_data

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
