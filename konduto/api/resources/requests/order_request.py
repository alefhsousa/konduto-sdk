import json
from dataclasses import dataclass, asdict
from datetime import datetime
from decimal import Decimal
from typing import Optional, List

from konduto.api.resources.address import Address
from konduto.api.resources.customer import Customer
from konduto.api.resources.payment import Payment
from konduto.api.resources.seller import Seller
from konduto.api.resources.shopping_cart import ShoppingCart
from konduto.api.resources.travel import Travel
from konduto.infrastructure.json_enconder import JsonEncoder


@dataclass
class OrderRequest:
    id: str
    visitor: str
    customer: Customer
    total_amount: Decimal
    analyze: Optional[bool] = True
    payment: Optional[List[Payment]] = None
    billing: Optional[Address] = None
    shipping: Optional[Address] = None
    shopping_cart: Optional[ShoppingCart] = None
    tavel: Optional[Travel] = None
    shipping_amount: Optional[Decimal] = None
    tax_amount: Optional[Decimal] = None
    currency: Optional[str] = None
    installments: Optional[int] = None
    ip: Optional[str] = None
    first_message: Optional[datetime] = None
    messages_exchanged: Optional[int] = None
    purchased_at: Optional[datetime] = None
    seller: Optional[Seller] = None

    @property
    def to_dict(self):
        return asdict(self)

    @property
    def json(self):
        return json.dumps(self.to_dict, cls=JsonEncoder)
