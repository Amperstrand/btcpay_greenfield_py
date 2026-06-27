from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.lightning_invoice_status import LightningInvoiceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lightning_invoice_data_custom_records_type_0 import LightningInvoiceDataCustomRecordsType0


T = TypeVar("T", bound="LightningInvoiceData")


@_attrs_define
class LightningInvoiceData:
    """
    Attributes:
        id (str | Unset): The invoice's ID
        status (LightningInvoiceStatus | Unset):
        bolt11 (str | Unset): The BOLT11 representation of the invoice
        paid_at (float | None | Unset): The unix timestamp when the invoice got paid
        expires_at (float | Unset): A unix timestamp in seconds Example: 1592312018.
        amount (str | Unset): The amount of the invoice in millisatoshi
        amount_received (str | Unset): The amount received in millisatoshi
        payment_hash (str | Unset): The payment hash
        preimage (None | str | Unset): The payment preimage (available when status is complete)
        custom_records (LightningInvoiceDataCustomRecordsType0 | None | Unset): The custom TLV records attached to a
            keysend payment
    """

    id: str | Unset = UNSET
    status: LightningInvoiceStatus | Unset = UNSET
    bolt11: str | Unset = UNSET
    paid_at: float | None | Unset = UNSET
    expires_at: float | Unset = UNSET
    amount: str | Unset = UNSET
    amount_received: str | Unset = UNSET
    payment_hash: str | Unset = UNSET
    preimage: None | str | Unset = UNSET
    custom_records: LightningInvoiceDataCustomRecordsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.lightning_invoice_data_custom_records_type_0 import LightningInvoiceDataCustomRecordsType0

        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        bolt11 = self.bolt11

        paid_at: float | None | Unset
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        else:
            paid_at = self.paid_at

        expires_at = self.expires_at

        amount = self.amount

        amount_received = self.amount_received

        payment_hash = self.payment_hash

        preimage: None | str | Unset
        if isinstance(self.preimage, Unset):
            preimage = UNSET
        else:
            preimage = self.preimage

        custom_records: dict[str, Any] | None | Unset
        if isinstance(self.custom_records, Unset):
            custom_records = UNSET
        elif isinstance(self.custom_records, LightningInvoiceDataCustomRecordsType0):
            custom_records = self.custom_records.to_dict()
        else:
            custom_records = self.custom_records

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if bolt11 is not UNSET:
            field_dict["BOLT11"] = bolt11
        if paid_at is not UNSET:
            field_dict["paidAt"] = paid_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_received is not UNSET:
            field_dict["amountReceived"] = amount_received
        if payment_hash is not UNSET:
            field_dict["paymentHash"] = payment_hash
        if preimage is not UNSET:
            field_dict["preimage"] = preimage
        if custom_records is not UNSET:
            field_dict["customRecords"] = custom_records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lightning_invoice_data_custom_records_type_0 import LightningInvoiceDataCustomRecordsType0

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: LightningInvoiceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LightningInvoiceStatus(_status)

        bolt11 = d.pop("BOLT11", UNSET)

        def _parse_paid_at(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        paid_at = _parse_paid_at(d.pop("paidAt", UNSET))

        expires_at = d.pop("expiresAt", UNSET)

        amount = d.pop("amount", UNSET)

        amount_received = d.pop("amountReceived", UNSET)

        payment_hash = d.pop("paymentHash", UNSET)

        def _parse_preimage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preimage = _parse_preimage(d.pop("preimage", UNSET))

        def _parse_custom_records(data: object) -> LightningInvoiceDataCustomRecordsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_records_type_0 = LightningInvoiceDataCustomRecordsType0.from_dict(data)

                return custom_records_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LightningInvoiceDataCustomRecordsType0 | None | Unset, data)

        custom_records = _parse_custom_records(d.pop("customRecords", UNSET))

        lightning_invoice_data = cls(
            id=id,
            status=status,
            bolt11=bolt11,
            paid_at=paid_at,
            expires_at=expires_at,
            amount=amount,
            amount_received=amount_received,
            payment_hash=payment_hash,
            preimage=preimage,
            custom_records=custom_records,
        )

        return lightning_invoice_data
