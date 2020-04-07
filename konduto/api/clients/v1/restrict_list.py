from typing import Union

from konduto import KONDUTO_DOMAIN
from konduto.api import KondutoHttpClient
from konduto.api.resources.requests.konduto_restrict_email_request import KondutoRestrictEmailRequest
from konduto.api.resources.response.konduto_error import KondutoError
from konduto.api.resources.response.restrict_email_response import KondutoRestrictEmailResponse, KondutoRestrictEmailResponseMapper

ENDPOINT = f'{KONDUTO_DOMAIN}v1/blacklist/email'.strip('/')


class KondutoRestrictClient(KondutoHttpClient):

    def create(self, payload: KondutoRestrictEmailRequest) -> Union[KondutoRestrictEmailResponse, KondutoError]:
        result = self.post(ENDPOINT, payload.json)

        if result.is_right:
            return KondutoRestrictEmailResponseMapper.to_model(result.value)

        return result.value

    def update(self, email: str, payload: KondutoRestrictEmailRequest):
        result = self.put(f'{ENDPOINT}/{email}', payload.json_to_update)

        if result.is_right:
            konduto_response = result.value
            konduto_response['email_address'] = email
            return KondutoRestrictEmailResponseMapper.to_model(konduto_response)

        return result.value

    def load(self, email):
        result = self.get(f'{ENDPOINT}/{email}')

        if result.is_right:
            return KondutoRestrictEmailResponseMapper.to_model(result.value)

        return result.value

    def remove(self, email: str):
        result = self.delete(f'{ENDPOINT}/{email}')

        if result.is_right:
            konduto_response = result.value
            konduto_response['email_address'] = email
            return KondutoRestrictEmailResponseMapper.to_model(konduto_response)

        return result.value
