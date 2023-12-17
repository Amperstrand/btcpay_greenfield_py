# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class InvoiceType(str, Enum):
    """
    The type of the invoice
    """

    """
    allowed enum values
    """
    STANDARD = 'Standard'
    TOPUP = 'TopUp'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InvoiceType from a JSON string"""
        return cls(json.loads(json_str))


