from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullPaymentsApprovePayoutBody")


@_attrs_define
class PullPaymentsApprovePayoutBody:
    """
    Attributes:
        revision (int | Unset): The revision number of the payout being modified
        rate_rule (None | str | Unset): The rate rule to calculate the rate of the payout. This can also be a fixed
            decimal. (if null or unspecified, will use the same rate setting as the store's settings) Example:
            kraken(BTC_USD).
    """

    revision: int | Unset = UNSET
    rate_rule: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision = self.revision

        rate_rule: None | str | Unset
        if isinstance(self.rate_rule, Unset):
            rate_rule = UNSET
        else:
            rate_rule = self.rate_rule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revision is not UNSET:
            field_dict["revision"] = revision
        if rate_rule is not UNSET:
            field_dict["rateRule"] = rate_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revision = d.pop("revision", UNSET)

        def _parse_rate_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rate_rule = _parse_rate_rule(d.pop("rateRule", UNSET))

        pull_payments_approve_payout_body = cls(
            revision=revision,
            rate_rule=rate_rule,
        )

        pull_payments_approve_payout_body.additional_properties = d
        return pull_payments_approve_payout_body

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
