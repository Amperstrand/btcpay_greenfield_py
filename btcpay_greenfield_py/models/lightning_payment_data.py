from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.lightning_payment_status import LightningPaymentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LightningPaymentData")


@_attrs_define
class LightningPaymentData:
    """
    Attributes:
        id (str | Unset): The payment's ID
        status (LightningPaymentStatus | Unset):
        bolt11 (str | Unset): The BOLT11 representation of the payment
        payment_hash (str | Unset): The payment hash
        preimage (str | Unset): The payment preimage (available when status is complete)
        created_at (float | None | Unset): The unix timestamp when the payment got created
        total_amount (str | Unset): The total amount (including fees) in millisatoshi
        fee_amount (str | Unset): The total fees in millisatoshi
    """

    id: str | Unset = UNSET
    status: LightningPaymentStatus | Unset = UNSET
    bolt11: str | Unset = UNSET
    payment_hash: str | Unset = UNSET
    preimage: str | Unset = UNSET
    created_at: float | None | Unset = UNSET
    total_amount: str | Unset = UNSET
    fee_amount: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        bolt11 = self.bolt11

        payment_hash = self.payment_hash

        preimage = self.preimage

        created_at: float | None | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        total_amount = self.total_amount

        fee_amount = self.fee_amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if bolt11 is not UNSET:
            field_dict["BOLT11"] = bolt11
        if payment_hash is not UNSET:
            field_dict["paymentHash"] = payment_hash
        if preimage is not UNSET:
            field_dict["preimage"] = preimage
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if fee_amount is not UNSET:
            field_dict["feeAmount"] = fee_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: LightningPaymentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LightningPaymentStatus(_status)

        bolt11 = d.pop("BOLT11", UNSET)

        payment_hash = d.pop("paymentHash", UNSET)

        preimage = d.pop("preimage", UNSET)

        def _parse_created_at(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        total_amount = d.pop("totalAmount", UNSET)

        fee_amount = d.pop("feeAmount", UNSET)

        lightning_payment_data = cls(
            id=id,
            status=status,
            bolt11=bolt11,
            payment_hash=payment_hash,
            preimage=preimage,
            created_at=created_at,
            total_amount=total_amount,
            fee_amount=fee_amount,
        )

        return lightning_payment_data
