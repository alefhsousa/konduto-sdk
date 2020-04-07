from enum import Enum, unique


@unique
class KondutoOrderStatus(Enum):
    APPROVED = 'approved'
    DECLINED = 'declined'
    NOT_AUTHORIZED = 'not_authorized'
    CANCELED = 'canceled'
    FRAUD = 'fraud'
