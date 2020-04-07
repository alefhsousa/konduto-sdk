from datetime import datetime, date
from decimal import Decimal


def date_str_to_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%Y-%m-%d').date()


def float_to_decimal(float_number: str) -> Decimal:
    return Decimal(str(float_number))


def datetime_str_to_datetime(datetime_str: str) -> datetime:
    return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')


def to_int(int_str: str) -> int:
    return int(int_str)
