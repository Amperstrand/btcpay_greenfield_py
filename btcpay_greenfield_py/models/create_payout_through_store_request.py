from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_payout_through_store_request_metadata import CreatePayoutThroughStoreRequestMetadata


T = TypeVar("T", bound="CreatePayoutThroughStoreRequest")


@_attrs_define
class CreatePayoutThroughStoreRequest:
    """
    Attributes:
        destination (str | Unset): The destination of the payout (can be an address or a BIP21 url) Example:
            1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2.
        amount (str | Unset): The amount of the payout in the currency of the pull payment (eg. USD). Example: 10399.18.
        payment_method (str | Unset): Payment method IDs are a combination of crypto code and payment type. Available
            payment method IDs for Bitcoin are:
            - `"BTC-OnChain"` (with the equivalent of `"BTC"`)
            -`"BTC-LightningLike"`: Any supported LN-based payment method (Lightning or LNURL)
            - `"BTC-LightningNetwork"`: Lightning
            - `"BTC-LNURLPAY"`: LNURL

            Note: Separator can be either `-` or `_`.
        pull_payment_id (str | Unset): The pull payment to create this for. Optional.
        approved (bool | Unset): Whether to approve this payout automatically upon creation
        metadata (CreatePayoutThroughStoreRequestMetadata | Unset): Additional metadata to store with the payout
    """

    destination: str | Unset = UNSET
    amount: str | Unset = UNSET
    payment_method: str | Unset = UNSET
    pull_payment_id: str | Unset = UNSET
    approved: bool | Unset = UNSET
    metadata: CreatePayoutThroughStoreRequestMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination = self.destination

        amount = self.amount

        payment_method = self.payment_method

        pull_payment_id = self.pull_payment_id

        approved = self.approved

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if pull_payment_id is not UNSET:
            field_dict["pullPaymentId"] = pull_payment_id
        if approved is not UNSET:
            field_dict["approved"] = approved
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_payout_through_store_request_metadata import CreatePayoutThroughStoreRequestMetadata

        d = dict(src_dict)
        destination = d.pop("destination", UNSET)

        amount = d.pop("amount", UNSET)

        payment_method = d.pop("paymentMethod", UNSET)

        pull_payment_id = d.pop("pullPaymentId", UNSET)

        approved = d.pop("approved", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreatePayoutThroughStoreRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreatePayoutThroughStoreRequestMetadata.from_dict(_metadata)

        create_payout_through_store_request = cls(
            destination=destination,
            amount=amount,
            payment_method=payment_method,
            pull_payment_id=pull_payment_id,
            approved=approved,
            metadata=metadata,
        )

        create_payout_through_store_request.additional_properties = d
        return create_payout_through_store_request

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
