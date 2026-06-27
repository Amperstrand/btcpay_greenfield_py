from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PointOfSaleAppDataItems")


@_attrs_define
class PointOfSaleAppDataItems:
    """JSON object of app items

    Example:
        [{'description': "Lovely, fresh and tender, Meng Ding Gan Lu ('sweet dew') is grown in the lush Meng Ding
            Mountains of the southwestern province of Sichuan where it has been cultivated for over a thousand years.",
            'id': 'green tea', 'image': '~/img/pos-sample/green-tea.jpg', 'price': {'type': 2, 'formatted': '$1.00',
            'value': 1}, 'title': 'Green Tea', 'buyButtonText': None, 'inventory': 5, 'paymentMethods': None, 'disabled':
            False}, {'description': "Tian Jian Tian Jian means 'heavenly tippy tea' in Chinese, and it describes the finest
            grade of dark tea. Our Tian Jian dark tea is from Hunan province which is famous for making some of the best
            dark teas available.", 'id': 'black tea', 'image': '~/img/pos-sample/black-tea.jpg', 'price': {'type': 2,
            'formatted': '$1.00', 'value': 1}, 'title': 'Black Tea', 'buyButtonText': 'Test Buy Button Text', 'inventory':
            None, 'paymentMethods': None, 'disabled': False}]

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        point_of_sale_app_data_items = cls()

        point_of_sale_app_data_items.additional_properties = d
        return point_of_sale_app_data_items

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
