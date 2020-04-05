from datetime import datetime
from decimal import Decimal


def date_str_to_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()


def float_to_decimal(float_number):
    return Decimal(str(float_number))


def datetime_str_to_datetime(datetime_str):
    return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')
