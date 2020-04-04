import json
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional, Iterable

from konduto.api.resources.billing import Billing
from konduto.api.resources.customer import Customer
from konduto.api.resources.payment import Payment
from konduto.api.resources.seller import Seller
from konduto.api.resources.shipping import Shipping
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
    payment: Optional[Iterable[Payment]] = None
    billing: Optional[Billing] = None
    shipping: Optional[Shipping] = None
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
    def json(self):
        return json.dumps({'id': self.id,
                           'visitor': self.visitor,
                           'total_amount': self.total_amount,
                           'shipping_amount': self.shipping_amount,
                           'tax_amount': self.tax_amount,
                           'currency': self.currency,
                           'installments': self.installments,
                           'ip': self.ip,
                           'first_message': self.first_message,
                           'messages_exchanged': self.messages_exchanged,
                           'purchased_at': self.purchased_at,
                           'analyze': self.analyze,
                           'customer': self.customer.to_dict if self.customer else None,
                           'payment': [item.to_dict for item in self.payment] if self.payment else None,
                           'billing': self.billing.to_dict if self.billing else None,
                           'shipping': self.shipping.to_dict if self.shipping else None,
                           'shopping_cart': self.shopping_cart.to_dict if self.shopping_cart else None,
                           'travel': None,
                           'seller': self.seller.to_dict if self.seller else None}, cls=JsonEncoder)
