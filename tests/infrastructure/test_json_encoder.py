import json
import uuid
from datetime import datetime
from decimal import Decimal

from konduto.api.resources.order_status import OrderStatus
from konduto.infrastructure.json_enconder import JsonEncoder


class TestJsonEnconder:

    def test_should_parse_uuid(self):
        expect_result = uuid.uuid4()
        assert str(expect_result) in json.dumps({'uuid': expect_result}, cls=JsonEncoder)

    def test_should_parse_enum(self):
        expect_result = OrderStatus.APPROVED
        assert expect_result.name in json.dumps({'status': expect_result}, cls=JsonEncoder)

    def test_should_parse_datetime_iso8601(self):
        date = datetime(year=2020, month=4, day=1)
        expect_result = '2020-04-01T00:00:00Z'
        assert expect_result in json.dumps({'date': date}, cls=JsonEncoder)

    def test_should_parse_date_iso8601(self):
        date = datetime(year=2020, month=4, day=1)
        expect_result = '2020-04-01'
        assert expect_result in json.dumps({'date': date}, cls=JsonEncoder)

    def test_should_parse_decimal(self):
        decimal_value = '20.2124'
        assert decimal_value in json.dumps({'date': Decimal(decimal_value)}, cls=JsonEncoder)
