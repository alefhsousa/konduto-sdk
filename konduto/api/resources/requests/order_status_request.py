import json
from dataclasses import dataclass
from typing import Optional

from konduto.api.resources.order_status import OrderStatus


@dataclass
class OrderStatusRequest:
    status: OrderStatus
    comments: Optional[str] = None

    @property
    def json(self) -> str:
        return json.dumps(self.__dict__)
