from enum import Enum, unique


@unique
class OrderStatus(Enum):
    APPROVED = 'approved'
    DECLINED = 'declined'
    NOT_AUTHORIZED = 'not_authorized'
    CANCELED = 'canceled'
    FRAUD = 'fraud'
