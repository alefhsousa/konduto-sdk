import json

import requests_mock
from pytest import fixture

from konduto import KONDUTO_DOMAIN
from konduto.api.resources.konduto_order_status import KondutoOrderStatus
from konduto.api.resources.konduto_payment import KondutoPaymentType
from konduto.api.resources.response.konduto_error import KondutoError
from konduto.api.resources.response.konduto_order_response import KondutoRecommendation, KondutoOrderResponse
from konduto.client import KondutoClient
from konduto.infrastructure.either import Right, Left
from konduto.infrastructure.json_enconder import JsonEncoder
from tests.fixtures.request_factories import OrderRequestFactory, PaymentFactory
from tests.fixtures.response_factories import OrderResponseFactory

API_ENDPOINT_MOCK = f'{KONDUTO_DOMAIN}v1/orders'.strip('/')

MOCKED_ERROR_RESPONSE = {
    "status": "error",
    "message": {
        "where": "/",
        "why": {
            "expected": ["integer"],
            "found": "string"
        }
    }}

MOCKED_INTERNAL_ERROR_RESPONSE = {
    "status": "error",
    "message": {
        "notification": "We've been notified about this error and will investigate it.",
        "error_identifier": "09e1a98c-eada-4695-8864-bff8ba4707ba",
        "where": "/",
        "why": {
            "expected": ["ok"],
            "found": "Internal error"
        }
    }}


class TestOrderClient:

    @fixture
    def order_client(self):
        client = KondutoClient(private_key='someKey')
        return client

    def test_should_create_an_order(self, order_client):
        expected_response = OrderResponseFactory(id='123', score=0.42,
                                                 recommendation=KondutoRecommendation.APPROVE,
                                                 status=KondutoOrderStatus.APPROVED)

        order = OrderRequestFactory(payment=[PaymentFactory(type=KondutoPaymentType.CREDIT)])
        mocked_response = {'status': 'ok', 'order': expected_response.to_dict}
        mocked_response = json.dumps(mocked_response, cls=JsonEncoder)

        with requests_mock.mock() as mock:
            mock.post(API_ENDPOINT_MOCK, text=mocked_response)
            result = order_client.order.create(order)
            assert result
            assert isinstance(result, Right)
            assert isinstance(result.value, KondutoOrderResponse)
            response = result.value
            assert response.analyze is True
            assert response.id == expected_response.id
            assert response.recommendation == expected_response.recommendation
            assert response.score == expected_response.score
            assert response.status == expected_response.status

    def test_should_return_mapped_error_when_something_wrong_happens(self, order_client):
        order = OrderRequestFactory()
        mocked_response = json.dumps(MOCKED_ERROR_RESPONSE, cls=JsonEncoder)

        with requests_mock.mock() as mock:
            mock.post(API_ENDPOINT_MOCK, text=mocked_response, status_code=400)
            result = order_client.order.create(order)
            assert result
            assert isinstance(result, Left)
            assert isinstance(result.value, KondutoError)
            response = result.value
            assert MOCKED_ERROR_RESPONSE['status'] == response.status

    def test_should_return_mapped_error_with_id_when_internal_error_happens(self, order_client):
        order = OrderRequestFactory(payment=[PaymentFactory(type=KondutoPaymentType.TRANSFER)])
        mocked_response = json.dumps(MOCKED_INTERNAL_ERROR_RESPONSE, cls=JsonEncoder)

        with requests_mock.mock() as mock:
            mock.post(API_ENDPOINT_MOCK, text=mocked_response, status_code=500)
            result = order_client.order.create(order)
            assert result
            assert isinstance(result, Left)
            assert isinstance(result.value, KondutoError)
            response = result.value
            assert response.status == MOCKED_INTERNAL_ERROR_RESPONSE['status']
            assert response.message.error_identifier == MOCKED_INTERNAL_ERROR_RESPONSE['message']['error_identifier']
            assert response.message.notification == MOCKED_INTERNAL_ERROR_RESPONSE['message']['notification']

    def test_should_return_an_order_by_id(self, order_client):
        fake_order_id = 'fake123'
        expected_response = OrderResponseFactory(id=fake_order_id)
        mocked_response = {'status': 'ok', 'order': expected_response.to_dict}
        mocked_response = json.dumps(mocked_response, cls=JsonEncoder)
        with requests_mock.mock() as mock:
            mock.get(f'{API_ENDPOINT_MOCK}/{fake_order_id}', text=mocked_response)
            result = order_client.order.load(fake_order_id)
            assert result
            assert isinstance(result, Right)
            assert isinstance(result.value, KondutoOrderResponse)
            response = result.value
            assert response.id == expected_response.id
