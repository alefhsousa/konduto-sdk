import enum
import json
from decimal import Decimal
from uuid import UUID
from datetime import datetime, date, time, timedelta


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, enum.Enum):
            return obj.name
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        if isinstance(obj, (date, time)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)

        return json.JSONEncoder.default(self, obj)
