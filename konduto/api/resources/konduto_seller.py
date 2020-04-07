from dataclasses import dataclass, asdict
from datetime import date
from typing import Optional


@dataclass
class KondutoSeller:
    id: Optional[str]
    name: Optional[str]
    created_at: Optional[date]

    @property
    def to_dict(self) -> dict:
        return asdict(self)
