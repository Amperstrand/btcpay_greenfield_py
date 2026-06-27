from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreRateResult")


@_attrs_define
class StoreRateResult:
    """
    Attributes:
        currency_pair (str | Unset): Currency pair in the format of `BTC_USD` Example: BTC_USD.
        errors (list[str] | None | Unset): Errors relating to this currency pair fetching based on your config
        rate (str | Unset): the rate fetched based on the currency pair Example: 64392.23.
    """

    currency_pair: str | Unset = UNSET
    errors: list[str] | None | Unset = UNSET
    rate: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        currency_pair = self.currency_pair

        errors: list[str] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = self.errors

        else:
            errors = self.errors

        rate = self.rate

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if currency_pair is not UNSET:
            field_dict["currencyPair"] = currency_pair
        if errors is not UNSET:
            field_dict["errors"] = errors
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_pair = d.pop("currencyPair", UNSET)

        def _parse_errors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = cast(list[str], data)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        rate = d.pop("rate", UNSET)

        store_rate_result = cls(
            currency_pair=currency_pair,
            errors=errors,
            rate=rate,
        )

        return store_rate_result
