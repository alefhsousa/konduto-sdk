from typing import Union

from konduto import KONDUTO_DOMAIN
from konduto.api import KondutoHttpClient
from konduto.api.resources.requests.restrict_email_request import RestrictEmailRequest
from konduto.api.resources.response.error import Error
from konduto.api.resources.response.restrict_email_response import RestrictEmailResponse, RestrictEmailResponseMapper

ENDPOINT = f'{KONDUTO_DOMAIN}v1/blacklist/email'.strip('/')


class RestrictClientKonduto(KondutoHttpClient):

    def create(self, payload: RestrictEmailRequest) -> Union[RestrictEmailResponse, Error]:
        result = self.post(ENDPOINT, payload.json)

        if result.is_right:
            return RestrictEmailResponseMapper.to_model(result.value)

        return result.value

    def update(self, email: str, payload: RestrictEmailRequest):
        result = self.put(f'{ENDPOINT}/{email}', payload.json_to_update)

        if result.is_right:
            konduto_response = result.value
            konduto_response['email_address'] = email
            return RestrictEmailResponseMapper.to_model(konduto_response)

        return result.value

    def load(self, email):
        result = self.get(f'{ENDPOINT}/{email}')

        if result.is_right:
            return RestrictEmailResponseMapper.to_model(result.value)

        return result.value

    def remove(self, email: str):
        result = self.delete(f'{ENDPOINT}/{email}')

        if result.is_right:
            konduto_response = result.value
            konduto_response['email_address'] = email
            return RestrictEmailResponseMapper.to_model(konduto_response)

        return result.value
