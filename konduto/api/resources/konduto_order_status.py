from enum import Enum, unique


@unique
class KondutoOrderStatus(Enum):
    APPROVED = 'approved'
    PENDING = 'pending'
    DECLINED = 'declined'
    NOT_AUTHORIZED = 'not_authorized'
    CANCELED = 'canceled'
    FRAUD = 'fraud'
    NOT_ANALYZED = 'not_analyzed'

    @classmethod
    def from_string(cls, enum_str: str):
        return cls(str(enum_str).lower())
