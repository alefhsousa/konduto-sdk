from dataclasses import dataclass, asdict
from enum import Enum
from typing import Optional


class PaymentType(Enum):
    CREDIT = 'credit'
    BOLETO = 'boleto'
    DEBIT = 'debit'
    TRANSFER = 'transfer'
    VOUCHER = 'voucher'


class PaymentStatus(Enum):
    APPROVED = 'approved'
    DECLINED = 'declined'
    PENDING = 'pending'


@dataclass
class Payment:
    type: PaymentType
    status: PaymentStatus
    bin: Optional[str] = None
    last4: Optional[str] = None
    expiration_date: Optional[str] = None

    @property
    def to_dict(self) -> dict:
        return asdict(self)
