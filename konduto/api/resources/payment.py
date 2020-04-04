from dataclasses import dataclass, asdict
from enum import Enum
from typing import Optional


class PaymentType(Enum):
    CREDIT = 'CREDIT'
    BOLETO = 'BOLETO'
    DEBIT = 'DEBIT'
    TRANSFER = 'TRANSFER'
    VOUCHER = 'VOUCHER'


class PaymentStatus(Enum):
    APPROVED = 'APPROVED'
    DECLINED = 'DECLINED'
    PENDING = 'PENDING'


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
