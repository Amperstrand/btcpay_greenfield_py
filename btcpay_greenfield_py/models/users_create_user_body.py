from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsersCreateUserBody")


@_attrs_define
class UsersCreateUserBody:
    """
    Attributes:
        email (str | Unset): The email of the new user
        password (None | str | Unset): The password of the new user (if no password is set, an email will be sent to the
            user requiring him to set the password)
        is_administrator (bool | None | Unset): Make this user administrator (only if you have the `unrestricted`
            permission of a server administrator) Default: False.
    """

    email: str | Unset = UNSET
    password: None | str | Unset = UNSET
    is_administrator: bool | None | Unset = False

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        is_administrator: bool | None | Unset
        if isinstance(self.is_administrator, Unset):
            is_administrator = UNSET
        else:
            is_administrator = self.is_administrator

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if is_administrator is not UNSET:
            field_dict["isAdministrator"] = is_administrator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_is_administrator(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_administrator = _parse_is_administrator(d.pop("isAdministrator", UNSET))

        users_create_user_body = cls(
            email=email,
            password=password,
            is_administrator=is_administrator,
        )

        return users_create_user_body
