from dataclasses import dataclass, asdict
from datetime import date
from typing import Optional


@dataclass
class Customer:
    id: str
    name: str
    email: str
    dob: Optional[date] = None
    phone1: Optional[str] = None
    phone2: Optional[str] = None
    tax_id: Optional[str] = None
    created_at: Optional[date] = None
    new: Optional[bool] = None
    vip: Optional[bool] = None

    @property
    def to_dict(self) -> dict:
        return asdict(self)
