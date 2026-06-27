from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CrowdfundAppDataPerks")


@_attrs_define
class CrowdfundAppDataPerks:
    """JSON of perks available in the app

    Example:
        [{'description': None, 'id': 'test perk', 'image': None, 'price': {'type': 2, 'formatted': '$100.00', 'value':
            100}, 'title': 'test perk', 'buyButtonText': None, 'inventory': None, 'paymentMethods': None, 'disabled':
            False}, {'description': 'this is an amazing perk', 'id': 'test test', 'image':
            'https://mainnet.demo.btcpayserver.org/img/errorpages/404_nicolas.jpg', 'price': {'type': 1, 'formatted':
            '$69.42', 'value': 69.42}, 'title': 'test test', 'buyButtonText': None, 'inventory': 5, 'paymentMethods': None,
            'disabled': False}, {'description': None, 'id': 'f$t45hj764325', 'image': None, 'price': {'type': 0,
            'formatted': None, 'value': None}, 'title': 'amazing perk', 'buyButtonText': 'button text', 'inventory': None,
            'paymentMethods': None, 'disabled': True}]

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crowdfund_app_data_perks = cls()

        crowdfund_app_data_perks.additional_properties = d
        return crowdfund_app_data_perks

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
