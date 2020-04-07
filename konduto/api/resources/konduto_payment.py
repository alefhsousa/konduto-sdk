from dataclasses import dataclass, asdict
from enum import Enum
from typing import Optional


class KondutoPaymentType(Enum):
    CREDIT = 'credit'
    BOLETO = 'boleto'
    DEBIT = 'debit'
    TRANSFER = 'transfer'
    VOUCHER = 'voucher'


class KondutoPaymentStatus(Enum):
    APPROVED = 'approved'
    DECLINED = 'declined'
    PENDING = 'pending'


@dataclass
class KondutoPayment:
    type: KondutoPaymentType
    status: KondutoPaymentStatus
    bin: Optional[str] = None
    last4: Optional[str] = None
    expiration_date: Optional[str] = None

    @property
    def to_dict(self) -> dict:
        return asdict(self)
