from enum import Enum, unique


@unique
class OrderStatus(Enum):
    APPROVED = 'APPROVED'
    DECLINED = 'DECLINED'
    NOT_AUTHORIZED = 'NOT_AUTHORIZED'
    CANCELED = 'CANCELED'
    FRAUD = 'FRAUD'
