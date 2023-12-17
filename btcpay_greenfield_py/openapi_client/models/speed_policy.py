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


class SpeedPolicy(str, Enum):
    """
    This is a risk mitigation parameter for the merchant to configure how they want to fulfill orders depending on the number of block confirmations for the transaction made by the consumer on the selected cryptocurrency. `\"HighSpeed\"`: 0 confirmations (1 confirmation if RBF enabled in transaction)    `\"MediumSpeed\"`: 1 confirmation    `\"LowMediumSpeed\"`: 2 confirmations    `\"LowSpeed\"`: 6 confirmations 
    """

    """
    allowed enum values
    """
    HIGHSPEED = 'HighSpeed'
    LOWMEDIUMSPEED = 'LowMediumSpeed'
    LOWSPEED = 'LowSpeed'
    MEDIUMSPEED = 'MediumSpeed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SpeedPolicy from a JSON string"""
        return cls(json.loads(json_str))


