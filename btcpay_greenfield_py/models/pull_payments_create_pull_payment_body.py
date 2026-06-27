from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullPaymentsCreatePullPaymentBody")


@_attrs_define
class PullPaymentsCreatePullPaymentBody:
    """
    Attributes:
        name (None | str | Unset): The name of the pull payment
        description (None | str | Unset): The description of the pull payment
        amount (str | Unset): The amount in `currency` of this pull payment as a decimal string Example: 0.1.
        currency (str | Unset): The currency of the amount. Example: BTC.
        period (int | None | Unset): The length of each period in seconds. Example: 604800.
        bolt11_expiration (None | str | Unset): If lightning is activated, do not accept BOLT11 invoices with expiration
            less than … days Default: '30'. Example: 30.
        auto_approve_claims (bool | None | Unset): Any payouts created for this pull payment will skip the approval
            phase upon creation Default: False.
        starts_at (int | None | Unset): When this pull payment is effective. Already started if null or unspecified.
            Example: 1592312018.
        expires_at (int | None | Unset): When this pull payment expires. Never expires if null or unspecified. Example:
            1593129600.
        payment_methods (list[str] | Unset): The list of supported payment methods supported by this pull payment.
            Available options can be queried from the `StorePaymentMethods_GetStorePaymentMethods` endpoint
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    period: int | None | Unset = UNSET
    bolt11_expiration: None | str | Unset = "30"
    auto_approve_claims: bool | None | Unset = False
    starts_at: int | None | Unset = UNSET
    expires_at: int | None | Unset = UNSET
    payment_methods: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        amount = self.amount

        currency = self.currency

        period: int | None | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        else:
            period = self.period

        bolt11_expiration: None | str | Unset
        if isinstance(self.bolt11_expiration, Unset):
            bolt11_expiration = UNSET
        else:
            bolt11_expiration = self.bolt11_expiration

        auto_approve_claims: bool | None | Unset
        if isinstance(self.auto_approve_claims, Unset):
            auto_approve_claims = UNSET
        else:
            auto_approve_claims = self.auto_approve_claims

        starts_at: int | None | Unset
        if isinstance(self.starts_at, Unset):
            starts_at = UNSET
        else:
            starts_at = self.starts_at

        expires_at: int | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        payment_methods: list[str] | Unset = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if period is not UNSET:
            field_dict["period"] = period
        if bolt11_expiration is not UNSET:
            field_dict["BOLT11Expiration"] = bolt11_expiration
        if auto_approve_claims is not UNSET:
            field_dict["autoApproveClaims"] = auto_approve_claims
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if payment_methods is not UNSET:
            field_dict["paymentMethods"] = payment_methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        def _parse_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period = _parse_period(d.pop("period", UNSET))

        def _parse_bolt11_expiration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bolt11_expiration = _parse_bolt11_expiration(d.pop("BOLT11Expiration", UNSET))

        def _parse_auto_approve_claims(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_approve_claims = _parse_auto_approve_claims(d.pop("autoApproveClaims", UNSET))

        def _parse_starts_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        starts_at = _parse_starts_at(d.pop("startsAt", UNSET))

        def _parse_expires_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        payment_methods = cast(list[str], d.pop("paymentMethods", UNSET))

        pull_payments_create_pull_payment_body = cls(
            name=name,
            description=description,
            amount=amount,
            currency=currency,
            period=period,
            bolt11_expiration=bolt11_expiration,
            auto_approve_claims=auto_approve_claims,
            starts_at=starts_at,
            expires_at=expires_at,
            payment_methods=payment_methods,
        )

        pull_payments_create_pull_payment_body.additional_properties = d
        return pull_payments_create_pull_payment_body

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
