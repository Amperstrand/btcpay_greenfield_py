from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailSettingsData")


@_attrs_define
class EmailSettingsData:
    """
    Attributes:
        server (str | Unset): Smtp server host
        port (float | Unset): Smtp server port
        login (str | Unset): Smtp server username
        password (str | Unset): Smtp server password
        from_ (str | Unset): Email to send from
        from_display (str | Unset): The name of the sender
        disable_certificate_check (bool | Unset): Disable TLS certificate security checks Default: False.
    """

    server: str | Unset = UNSET
    port: float | Unset = UNSET
    login: str | Unset = UNSET
    password: str | Unset = UNSET
    from_: str | Unset = UNSET
    from_display: str | Unset = UNSET
    disable_certificate_check: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        server = self.server

        port = self.port

        login = self.login

        password = self.password

        from_ = self.from_

        from_display = self.from_display

        disable_certificate_check = self.disable_certificate_check

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server
        if port is not UNSET:
            field_dict["port"] = port
        if login is not UNSET:
            field_dict["login"] = login
        if password is not UNSET:
            field_dict["password"] = password
        if from_ is not UNSET:
            field_dict["from"] = from_
        if from_display is not UNSET:
            field_dict["fromDisplay"] = from_display
        if disable_certificate_check is not UNSET:
            field_dict["disableCertificateCheck"] = disable_certificate_check

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = d.pop("server", UNSET)

        port = d.pop("port", UNSET)

        login = d.pop("login", UNSET)

        password = d.pop("password", UNSET)

        from_ = d.pop("from", UNSET)

        from_display = d.pop("fromDisplay", UNSET)

        disable_certificate_check = d.pop("disableCertificateCheck", UNSET)

        email_settings_data = cls(
            server=server,
            port=port,
            login=login,
            password=password,
            from_=from_,
            from_display=from_display,
            disable_certificate_check=disable_certificate_check,
        )

        return email_settings_data
