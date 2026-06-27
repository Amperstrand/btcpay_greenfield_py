from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvoiceMetadata")


@_attrs_define
class InvoiceMetadata:
    """Additional information around the invoice that can be supplied. The mentioned properties are all optional and you
    can introduce any json format you wish. See [our
    documentation](https://docs.btcpayserver.org/Development/InvoiceMetadata/) for more information.

        Example:
            {'orderId': 'pos-app_346KRC5BjXXXo8cRFKwTBmdR6ZJ4', 'orderUrl':
                'https://localhost:14142/apps/346KRC5BjXXXo8cRFKwTBmdR6ZJ4/pos', 'itemDesc': 'Tea shop', 'posData': {'tip':
                0.48, 'cart': [{'id': 'pu erh', 'count': 1, 'image': '~/img/pos-sample/pu-erh.jpg', 'price': {'type': 2,
                'value': 2, 'formatted': '$2.00'}, 'title': 'Pu Erh', 'inventory': None}, {'id': 'rooibos', 'count': 1, 'image':
                '~/img/pos-sample/rooibos.jpg', 'price': {'type': 2, 'value': 1.2, 'formatted': '$1.20'}, 'title': 'Rooibos',
                'inventory': None}], 'total': 3.68, 'subTotal': 3.2, 'customAmount': 0, 'discountAmount': 0,
                'discountPercentage': 0}, 'receiptData': {'Tip': '$0.48', 'Cart': {'Pu Erh': '$2.00 x 1 = $2.00', 'Rooibos':
                '$1.20 x 1 = $1.20'}}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invoice_metadata = cls()

        invoice_metadata.additional_properties = d
        return invoice_metadata

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
