import json
from dataclasses import dataclass, asdict
from datetime import date
from typing import Optional

from konduto.infrastructure.json_enconder import JsonEncoder
from konduto.infrastructure.parsers import date_str_to_date, datetime_str_to_datetime


@dataclass
class RestrictEmailResponse:
    expires_at: date
    uri: Optional[str] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None
    email_address: Optional[str] = None
    message: Optional[str] = None

    @property
    def email(self):
        if self.email_address:
            return self.email_address
        elif self.uri:
            self.email_address = str(self.uri).split('/')[-1]
            return self.email_address
        else:
            return None

    @property
    def to_dict(self):
        return asdict(self)

    @property
    def json(self):
        return json.dumps(self.to_dict, cls=JsonEncoder)


class RestrictEmailResponseMapper:

    @staticmethod
    def to_model(payload: dict) -> RestrictEmailResponse:
        expires_at = date_str_to_date(payload['expires_at']) if payload.get('expires_at') else None
        created_at = datetime_str_to_datetime(payload['created_at']) if payload.get('created_at') else None
        updated_at = datetime_str_to_datetime(payload['updated_at']) if payload.get('updated_at') else None
        return RestrictEmailResponse(expires_at=expires_at, uri=payload.get('uri'), created_at=created_at,
                                     updated_at=updated_at, email_address=payload.get('email_address'),
                                     message=payload.get('message'))
