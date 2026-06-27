from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullPaymentData")


@_attrs_define
class PullPaymentData:
    """
    Attributes:
        id (str | Unset): Id of the pull payment
        name (str | Unset): Name given to pull payment when it was created
        description (str | Unset): Description given to pull payment when it was created
        currency (str | Unset): The currency of the pull payment's amount Example: BTC.
        amount (str | Unset): The amount in the currency of this pull payment as a decimal string Example: 1.12000000.
        period (int | None | Unset): The length of each period in seconds Example: 604800.
        bolt11_expiration (str | Unset): If lightning is activated, do not accept BOLT11 invoices with expiration less
            than … days Example: 30.
        auto_approve_claims (bool | None | Unset): Any payouts created for this pull payment will skip the approval
            phase upon creation Default: False.
        archived (bool | Unset): Whether this pull payment is archived
        view_link (str | Unset): The link to a page to claim payouts to this pull payment
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    currency: str | Unset = UNSET
    amount: str | Unset = UNSET
    period: int | None | Unset = UNSET
    bolt11_expiration: str | Unset = UNSET
    auto_approve_claims: bool | None | Unset = False
    archived: bool | Unset = UNSET
    view_link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        currency = self.currency

        amount = self.amount

        period: int | None | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        else:
            period = self.period

        bolt11_expiration = self.bolt11_expiration

        auto_approve_claims: bool | None | Unset
        if isinstance(self.auto_approve_claims, Unset):
            auto_approve_claims = UNSET
        else:
            auto_approve_claims = self.auto_approve_claims

        archived = self.archived

        view_link = self.view_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if period is not UNSET:
            field_dict["period"] = period
        if bolt11_expiration is not UNSET:
            field_dict["BOLT11Expiration"] = bolt11_expiration
        if auto_approve_claims is not UNSET:
            field_dict["autoApproveClaims"] = auto_approve_claims
        if archived is not UNSET:
            field_dict["archived"] = archived
        if view_link is not UNSET:
            field_dict["viewLink"] = view_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        def _parse_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period = _parse_period(d.pop("period", UNSET))

        bolt11_expiration = d.pop("BOLT11Expiration", UNSET)

        def _parse_auto_approve_claims(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_approve_claims = _parse_auto_approve_claims(d.pop("autoApproveClaims", UNSET))

        archived = d.pop("archived", UNSET)

        view_link = d.pop("viewLink", UNSET)

        pull_payment_data = cls(
            id=id,
            name=name,
            description=description,
            currency=currency,
            amount=amount,
            period=period,
            bolt11_expiration=bolt11_expiration,
            auto_approve_claims=auto_approve_claims,
            archived=archived,
            view_link=view_link,
        )

        pull_payment_data.additional_properties = d
        return pull_payment_data

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
