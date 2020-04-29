import json
from dataclasses import dataclass, asdict
from datetime import datetime
from decimal import Decimal
from enum import unique, Enum
from typing import Optional, List

from konduto.api.resources.konduto_address import KondutoAddress
from konduto.api.resources.konduto_customer import KondutoCustomer
from konduto.api.resources.konduto_order_status import KondutoOrderStatus
from konduto.api.resources.konduto_payment import KondutoPayment
from konduto.api.resources.konduto_seller import KondutoSeller
from konduto.api.resources.konduto_shopping_cart import KondutoProduct
from konduto.api.resources.kondutotravel import KondutoTravel
from konduto.infrastructure.json_enconder import JsonEncoder


@unique
class KondutoRecommendation(Enum):
    APPROVE = 'approve'
    REVIEW = 'review'
    DECLINE = 'decline'
    NONE = 'none'

    @classmethod
    def from_string(cls, enum_str: str):
        return cls(str(enum_str).lower())


@dataclass
class KondutoDevice:
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
class KondutoGeolocation:
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    @property
    def to_dict(self):
        return asdict(self)


@dataclass
class KondutoNavigation:
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
class KondutoOrderResponse:
    id: str
    score: float
    recommendation: KondutoRecommendation
    visitor: Optional[str] = True
    analyze: Optional[bool] = True
    status: Optional[KondutoOrderStatus] = None
    device: Optional[KondutoDevice] = None
    geolocation: Optional[KondutoGeolocation] = None
    navigation: Optional[KondutoNavigation] = None
    ip: Optional[str] = None
    customer: Optional[KondutoCustomer] = None
    payment: Optional[List[KondutoPayment]] = None
    billing: Optional[KondutoAddress] = None
    shipping: Optional[KondutoAddress] = None
    shopping_cart: Optional[List[KondutoProduct]] = None
    tavel: Optional[KondutoTravel] = None
    total_amount: Optional[Decimal] = None
    shipping_amount: Optional[Decimal] = None
    tax_amount: Optional[Decimal] = None
    currency: Optional[str] = None
    installments: Optional[int] = None
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
