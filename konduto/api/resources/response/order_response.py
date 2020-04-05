import json
from dataclasses import dataclass, asdict
from datetime import datetime
from decimal import Decimal
from enum import unique, Enum
from typing import Optional, List

from konduto.api.resources.billing import Billing
from konduto.api.resources.customer import Customer
from konduto.api.resources.order_status import OrderStatus
from konduto.api.resources.payment import Payment
from konduto.api.resources.seller import Seller
from konduto.api.resources.shipping import Shipping
from konduto.api.resources.shopping_cart import Product
from konduto.api.resources.travel import Travel
from konduto.infrastructure.json_enconder import JsonEncoder


@unique
class Recommendation(Enum):
    APPROVE = 'APPROVE'
    REVIEW = 'REVIEW'
    DECLINE = 'DECLINE'
    NONE = 'NONE'


@dataclass
class Device:
    user_id: Optional[str] = None
    fingerprint: Optional[str] = None
    platform: Optional[str] = None
    browser: Optional[str] = None
    language: Optional[str] = None
    timezone: Optional[str] = None
    cookie: Optional[bool] = False
    javascript: Optional[bool] = False
    flash: Optional[bool] = False

    @property
    def to_dict(self):
        return asdict(self)


@dataclass
class Geolocation:
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    @property
    def to_dict(self):
        return asdict(self)


@dataclass
class Navigation:
    time_site_7d: Optional[int] = None
    time_per_page_7d: Optional[int] = None
    new_accounts_7d: Optional[int] = None
    password_resets_7d: Optional[int] = None
    checkout_count_7d: Optional[int] = None
    sales_declined_7d: Optional[int] = None
    sessions_7d: Optional[int] = None
    time_site_1d: Optional[int] = None
    new_accounts_1d: Optional[int] = None
    password_resets_1d: Optional[int] = None
    sales_declined_1d: Optional[int] = None
    sessions_1d: Optional[int] = None
    session_time: Optional[int] = None
    time_since_last_sale: Optional[int] = None
    referrer: Optional[str] = None

    @property
    def to_dict(self):
        return asdict(self)


@dataclass
class OrderResponse:
    id: str
    score: float
    recommendation: Recommendation
    visitor: Optional[str] = True
    analyze: Optional[bool] = True
    status: Optional[OrderStatus] = None
    device: Optional[Device] = None
    geolocation: Optional[Geolocation] = None
    navigation: Optional[Navigation] = None
    ip: Optional[str] = None
    customer: Optional[Customer] = None
    payment: Optional[List[Payment]] = None
    billing: Optional[Billing] = None
    shipping: Optional[Shipping] = None
    shopping_cart: Optional[List[Product]] = None
    tavel: Optional[Travel] = None
    total_amount: Optional[Decimal] = None
    shipping_amount: Optional[Decimal] = None
    tax_amount: Optional[Decimal] = None
    currency: Optional[str] = None
    installments: Optional[int] = None
    first_message: Optional[datetime] = None
    messages_exchanged: Optional[int] = None
    purchased_at: Optional[datetime] = None
    seller: Optional[Seller] = None

    @property
    def to_dict(self):
        return {'id': self.id,
                'visitor': self.visitor,
                'total_amount': self.total_amount,
                'shipping_amount': self.shipping_amount,
                'tax_amount': self.tax_amount,
                'recommendation': self.recommendation,
                'score': self.score,
                'status': self.status,
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
                'shopping_cart': [item.to_dict for item in self.shopping_cart] if self.shopping_cart else None,
                'travel': None,
                'seller': self.seller.to_dict if self.seller else None,
                'device': self.device.to_dict if self.device else None,
                'geolocation': self.geolocation.json if self.device else None,
                'navigation': self.navigation.json if self.device else None}

    @property
    def json(self):
        return json.dumps(self.to_dict, cls=JsonEncoder)
