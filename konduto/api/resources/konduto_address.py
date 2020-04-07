from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class KondutoAddress:
    name: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None

    @property
    def to_dict(self):
        return asdict(self)
