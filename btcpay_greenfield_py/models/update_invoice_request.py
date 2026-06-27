from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_metadata import InvoiceMetadata


T = TypeVar("T", bound="UpdateInvoiceRequest")


@_attrs_define
class UpdateInvoiceRequest:
    """
    Attributes:
        metadata (InvoiceMetadata | Unset): Additional information around the invoice that can be supplied. The
            mentioned properties are all optional and you can introduce any json format you wish. See [our
            documentation](https://docs.btcpayserver.org/Development/InvoiceMetadata/) for more information. Example:
            {'orderId': 'pos-app_346KRC5BjXXXo8cRFKwTBmdR6ZJ4', 'orderUrl':
            'https://localhost:14142/apps/346KRC5BjXXXo8cRFKwTBmdR6ZJ4/pos', 'itemDesc': 'Tea shop', 'posData': {'tip':
            0.48, 'cart': [{'id': 'pu erh', 'count': 1, 'image': '~/img/pos-sample/pu-erh.jpg', 'price': {'type': 2,
            'value': 2, 'formatted': '$2.00'}, 'title': 'Pu Erh', 'inventory': None}, {'id': 'rooibos', 'count': 1, 'image':
            '~/img/pos-sample/rooibos.jpg', 'price': {'type': 2, 'value': 1.2, 'formatted': '$1.20'}, 'title': 'Rooibos',
            'inventory': None}], 'total': 3.68, 'subTotal': 3.2, 'customAmount': 0, 'discountAmount': 0,
            'discountPercentage': 0}, 'receiptData': {'Tip': '$0.48', 'Cart': {'Pu Erh': '$2.00 x 1 = $2.00', 'Rooibos':
            '$1.20 x 1 = $1.20'}}}.
    """

    metadata: InvoiceMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_metadata import InvoiceMetadata

        d = dict(src_dict)
        _metadata = d.pop("metadata", UNSET)
        metadata: InvoiceMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = InvoiceMetadata.from_dict(_metadata)

        update_invoice_request = cls(
            metadata=metadata,
        )

        return update_invoice_request
