import json
from dataclasses import dataclass, asdict
from datetime import datetime
from decimal import Decimal
from typing import Optional, List

from konduto.api.resources.konduto_address import KondutoAddress
from konduto.api.resources.konduto_customer import KondutoCustomer
from konduto.api.resources.konduto_payment import KondutoPayment
from konduto.api.resources.konduto_seller import KondutoSeller
from konduto.api.resources.konduto_shopping_cart import KondutoProduct
from konduto.api.resources.kondutotravel import KondutoTravel
from konduto.infrastructure.json_enconder import JsonEncoder


@dataclass
class KondutoOrderRequest:
    id: str
    total_amount: Decimal
    customer: KondutoCustomer
    visitor: Optional[str] = None
    analyze: Optional[bool] = True
    payment: Optional[List[KondutoPayment]] = None
    billing: Optional[KondutoAddress] = None
    shipping: Optional[KondutoAddress] = None
    shopping_cart: Optional[List[KondutoProduct]] = None
    tavel: Optional[KondutoTravel] = None
    shipping_amount: Optional[Decimal] = None
    tax_amount: Optional[Decimal] = None
    currency: Optional[str] = None
    installments: Optional[int] = None
    ip: Optional[str] = None
    first_message: Optional[datetime] = None
    messages_exchanged: Optional[int] = None
    purchased_at: Optional[datetime] = None
    seller: Optional[KondutoSeller] = None

    @property
    def to_dict(self):
        return asdict(self)

    @property
    def json(self):
        return json.dumps(self.to_dict, cls=JsonEncoder)
