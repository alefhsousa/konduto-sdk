import enum
import json
from datetime import datetime, date, time
from decimal import Decimal
from uuid import UUID


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, enum.Enum):
            return obj.value
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        if isinstance(obj, (date, time)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)

        return super(JsonEncoder, self).default(obj)
