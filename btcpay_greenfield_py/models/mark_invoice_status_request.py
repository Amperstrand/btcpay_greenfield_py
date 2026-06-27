from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.invoice_status_mark import InvoiceStatusMark
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkInvoiceStatusRequest")


@_attrs_define
class MarkInvoiceStatusRequest:
    """
    Attributes:
        status (InvoiceStatusMark | Unset):
    """

    status: InvoiceStatusMark | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: InvoiceStatusMark | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InvoiceStatusMark(_status)

        mark_invoice_status_request = cls(
            status=status,
        )

        return mark_invoice_status_request
