import json
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class RestrictEmailRequest:
    email_address: str
    days_to_expire: Optional[int] = None

    @property
    def to_dict(self) -> dict:
        return asdict(self)

    @property
    def json(self) -> str:
        return json.dumps(self.to_dict)

    @property
    def json_to_update(self) -> str:
        return json.dumps({'days_to_expire': self.days_to_expire})
