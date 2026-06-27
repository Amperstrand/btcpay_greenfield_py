from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.payment_status import PaymentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Payment")


@_attrs_define
class Payment:
    """
    Attributes:
        id (str | Unset): A unique identifier for this payment
        received_date (float | Unset): A unix timestamp in seconds Example: 1592312018.
        value (str | Unset): The value of the payment
        fee (str | Unset): The fee paid for the payment
        status (PaymentStatus | Unset): The status of the payment
        destination (str | Unset): The destination the payment was made to
    """

    id: str | Unset = UNSET
    received_date: float | Unset = UNSET
    value: str | Unset = UNSET
    fee: str | Unset = UNSET
    status: PaymentStatus | Unset = UNSET
    destination: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        received_date = self.received_date

        value = self.value

        fee = self.fee

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        destination = self.destination

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if received_date is not UNSET:
            field_dict["receivedDate"] = received_date
        if value is not UNSET:
            field_dict["value"] = value
        if fee is not UNSET:
            field_dict["fee"] = fee
        if status is not UNSET:
            field_dict["status"] = status
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        received_date = d.pop("receivedDate", UNSET)

        value = d.pop("value", UNSET)

        fee = d.pop("fee", UNSET)

        _status = d.pop("status", UNSET)
        status: PaymentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PaymentStatus(_status)

        destination = d.pop("destination", UNSET)

        payment = cls(
            id=id,
            received_date=received_date,
            value=value,
            fee=fee,
            status=status,
            destination=destination,
        )

        return payment
