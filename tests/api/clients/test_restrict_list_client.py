import json

import requests_mock
from pytest import fixture

from konduto import KONDUTO_DOMAIN
from konduto.api.resources.response.restrict_email_response import KondutoRestrictEmailResponse
from konduto.client import KondutoClient
from tests.fixtures.request_factories import RestrictEmailRequestFactory
from tests.fixtures.response_factories import RestrictEmailResponseFactory

API_ENDPOINT_MOCK = f'{KONDUTO_DOMAIN}v1/blacklist/email'.strip('/')


class TestRestrictListClient:

    @fixture
    def restrict_client(self):
        client = KondutoClient(private_key='some-key')
        return client

    def test_should_create_an_restrict_email(self, restrict_client):
        email_request = RestrictEmailRequestFactory()
        email_response = RestrictEmailResponseFactory(email_address=email_request.email_address)

        with requests_mock.mock() as mock:
            mock.post(API_ENDPOINT_MOCK, text=email_response.json)
            response = restrict_client.restrict.create(email_request)

            assert response.uri
            assert response.created_at
            assert response.expires_at
            assert response.email == email_request.email_address

    def test_should_return_an_restrict_email(self, restrict_client):
        expected_email = RestrictEmailRequestFactory().email_address
        email_response = RestrictEmailResponseFactory(email_address=expected_email)

        with requests_mock.mock() as mock:
            mock.get(f'{API_ENDPOINT_MOCK}/{expected_email}', text=email_response.json)
            response = restrict_client.restrict.load(expected_email)

            assert response
            assert isinstance(response, KondutoRestrictEmailResponse)
            assert response.email == expected_email

    def test_should_update_an_restrict_email(self, restrict_client):

        email_request = RestrictEmailRequestFactory()
        email_response = RestrictEmailResponseFactory(email_address=email_request.email_address)

        with requests_mock.mock() as mock:
            mock.put(f'{API_ENDPOINT_MOCK}/{email_request.email_address}', text=email_response.json)
            response = restrict_client.restrict.update(email_request.email_address, email_request)

            assert response
            assert isinstance(response, KondutoRestrictEmailResponse)
            assert response.email == email_request.email_address

    def test_should_delete_an_restrict_email(self, restrict_client):
        expected_email = RestrictEmailRequestFactory().email_address
        email_response = RestrictEmailResponseFactory(email_address=expected_email)

        with requests_mock.mock() as mock:
            mock.delete(f'{API_ENDPOINT_MOCK}/{expected_email}', text=email_response.json)
            response = restrict_client.restrict.remove(expected_email)

            assert response
            assert isinstance(response, KondutoRestrictEmailResponse)
            assert response.email == expected_email
            assert response.message
