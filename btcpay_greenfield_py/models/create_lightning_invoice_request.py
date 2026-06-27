from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLightningInvoiceRequest")


@_attrs_define
class CreateLightningInvoiceRequest:
    """
    Attributes:
        amount (str | Unset): Amount wrapped in a string, represented in a millistatoshi string. (1000 millisatoshi = 1
            satoshi)
        description (None | str | Unset): Description of the invoice in the BOLT11
        description_hash_only (bool | None | Unset): If `descriptionHashOnly` is `true` (default is `false`), then the
            BOLT11 returned contains a hash of the `description`, rather than the `description`, itself. This allows for
            much longer descriptions, but they must be communicated via some other mechanism. Default: False.
        expiry (float | Unset):  Example: 90.
        private_route_hints (bool | None | Unset): True if the invoice should include private route hints Default:
            False.
    """

    amount: str | Unset = UNSET
    description: None | str | Unset = UNSET
    description_hash_only: bool | None | Unset = False
    expiry: float | Unset = UNSET
    private_route_hints: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        description_hash_only: bool | None | Unset
        if isinstance(self.description_hash_only, Unset):
            description_hash_only = UNSET
        else:
            description_hash_only = self.description_hash_only

        expiry = self.expiry

        private_route_hints: bool | None | Unset
        if isinstance(self.private_route_hints, Unset):
            private_route_hints = UNSET
        else:
            private_route_hints = self.private_route_hints

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if description is not UNSET:
            field_dict["description"] = description
        if description_hash_only is not UNSET:
            field_dict["descriptionHashOnly"] = description_hash_only
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if private_route_hints is not UNSET:
            field_dict["privateRouteHints"] = private_route_hints

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_description_hash_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        description_hash_only = _parse_description_hash_only(d.pop("descriptionHashOnly", UNSET))

        expiry = d.pop("expiry", UNSET)

        def _parse_private_route_hints(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        private_route_hints = _parse_private_route_hints(d.pop("privateRouteHints", UNSET))

        create_lightning_invoice_request = cls(
            amount=amount,
            description=description,
            description_hash_only=description_hash_only,
            expiry=expiry,
            private_route_hints=private_route_hints,
        )

        create_lightning_invoice_request.additional_properties = d
        return create_lightning_invoice_request

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
