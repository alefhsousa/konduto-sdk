from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Union

from dacite import from_dict, Config

from konduto import KONDUTO_DOMAIN
from konduto.api.clients import KondutoHttpClient
from konduto.api.resources.konduto_order_status import KondutoOrderStatus
from konduto.api.resources.requests.konduto_order_request import KondutoOrderRequest
from konduto.api.resources.requests.konduto_order_status_request import KondutoOrderStatusRequest
from konduto.api.resources.response.konduto_error import KondutoError
from konduto.api.resources.response.konduto_order_response import KondutoOrderResponse, KondutoRecommendation
from konduto.infrastructure.parsers import datetime_str_to_datetime, float_to_decimal, date_str_to_date

ENDPOINT = f'{KONDUTO_DOMAIN}v1/orders'.strip('/')


class KondutoOrderClient(KondutoHttpClient):

    def create(self, payload: KondutoOrderRequest) -> Union[KondutoOrderResponse, KondutoError]:
        result = self.post(ENDPOINT, payload.json)

        if result.is_right:
            response_order = result.value['order']
            order_response = KondutoOrderResponse(id=response_order['id'], score=response_order['score'],
                                                  recommendation=KondutoRecommendation(response_order['recommendation']),
                                                  status=KondutoOrderStatus(str(response_order['status']).lower()))
            return order_response

        return result.value

    def change_status(self, order_id: str, payload: KondutoOrderStatusRequest) -> Union[dict, KondutoError]:
        result = self.put(f'{ENDPOINT}/{order_id}', payload.json)

        if result.is_right:
            return result.value

        return result.value

    def load(self, order_id: str) -> Union[KondutoOrderResponse, KondutoError]:
        result = self.get(f'{ENDPOINT}/{order_id}')

        if result.is_right:
            return from_dict(data_class=KondutoOrderResponse, data=result.value['order'],
                             config=Config(cast=[Enum, int],
                                           type_hooks={date: date_str_to_date,
                                                       Decimal: float_to_decimal,
                                                       datetime: datetime_str_to_datetime,
                                                       int: lambda x: int(x)}))

        return result.value
