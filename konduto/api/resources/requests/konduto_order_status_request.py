import json
from dataclasses import dataclass
from typing import Optional

from konduto.api.resources.konduto_order_status import KondutoOrderStatus


@dataclass
class KondutoOrderStatusRequest:
    status: KondutoOrderStatus
    comments: Optional[str] = None

    @property
    def json(self) -> str:
        return json.dumps(dict(status=self.status.value, comments=self.comments or ""))
