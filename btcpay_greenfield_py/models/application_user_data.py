from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationUserData")


@_attrs_define
class ApplicationUserData:
    """
    Attributes:
        id (str | Unset): The id of the user
        email (str | Unset): The email of the user
        email_confirmed (bool | Unset): True if the email has been confirmed by the user
        requires_email_confirmation (bool | Unset): True if the email requires email confirmation to log in
        created (float | None | Unset): The creation date of the user as a unix timestamp. Null if created before
            v1.0.5.6
        roles (list[str] | Unset): The roles of the user
    """

    id: str | Unset = UNSET
    email: str | Unset = UNSET
    email_confirmed: bool | Unset = UNSET
    requires_email_confirmation: bool | Unset = UNSET
    created: float | None | Unset = UNSET
    roles: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        email_confirmed = self.email_confirmed

        requires_email_confirmation = self.requires_email_confirmation

        created: float | None | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        else:
            created = self.created

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if email_confirmed is not UNSET:
            field_dict["emailConfirmed"] = email_confirmed
        if requires_email_confirmation is not UNSET:
            field_dict["requiresEmailConfirmation"] = requires_email_confirmation
        if created is not UNSET:
            field_dict["created"] = created
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        email_confirmed = d.pop("emailConfirmed", UNSET)

        requires_email_confirmation = d.pop("requiresEmailConfirmation", UNSET)

        def _parse_created(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        roles = cast(list[str], d.pop("roles", UNSET))

        application_user_data = cls(
            id=id,
            email=email,
            email_confirmed=email_confirmed,
            requires_email_confirmation=requires_email_confirmation,
            created=created,
            roles=roles,
        )

        return application_user_data
