from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LightningAddressData")


@_attrs_define
class LightningAddressData:
    """
    Attributes:
        username (str | Unset): The username of the lightning address
        currency_code (None | str | Unset): The currency to generate the invoices for this lightning address in. Leave
            null lto use the store default.
        min_ (None | str | Unset): The minimum amount in sats this ln address allows
        max_ (None | str | Unset): The maximum amount in sats this ln address allows
    """

    username: str | Unset = UNSET
    currency_code: None | str | Unset = UNSET
    min_: None | str | Unset = UNSET
    max_: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        min_: None | str | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        max_: None | str | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        def _parse_min_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        def _parse_max_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        lightning_address_data = cls(
            username=username,
            currency_code=currency_code,
            min_=min_,
            max_=max_,
        )

        return lightning_address_data
