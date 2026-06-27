from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailData")


@_attrs_define
class EmailData:
    """
    Attributes:
        email (str | Unset): Email of the recipient
        subject (str | Unset): Subject of the email
        body (str | Unset): Body of the email to send as plain text.
    """

    email: str | Unset = UNSET
    subject: str | Unset = UNSET
    body: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        subject = self.subject

        body = self.body

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        email_data = cls(
            email=email,
            subject=subject,
            body=body,
        )

        return email_data
