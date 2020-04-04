from dataclasses import dataclass
from typing import Iterable, Optional

from dacite import from_dict


@dataclass
class Why:
    expected: Optional[str]
    found: Optional[str]
    missing: Optional[Iterable[str]]


@dataclass
class Message:
    where: str
    why: Why
    error_identifier: Optional[str]
    notification: Optional[str]


@dataclass
class Error:
    status: str
    message: Message

    @staticmethod
    def error_from_dict(response_dict: dict):
        return from_dict(data_class=Error, data=response_dict)
