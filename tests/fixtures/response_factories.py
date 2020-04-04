import random
import uuid

import factory
from factory import lazy_attribute, SubFactory
from faker import Faker

from konduto.api.resources.order_status import OrderStatus
from konduto.api.resources.response.order_response import OrderResponse, Recommendation
from tests.fixtures.request_factories import CustomerFactory, BillingFactory, ShippingFactory, ShoppingCartFactory, \
    PaymentFactory, SellerFactory, ProductFactory

fake = Faker()


class OrderResponseFactory(factory.Factory):
    class Meta:
        model = OrderResponse

    id = lazy_attribute(lambda o: uuid.uuid4())
    score = lazy_attribute(lambda o: fake.pyfloat(left_digits=None, right_digits=2,
                                                  positive=True, min_value=0, max_value=1))
    recommendation = lazy_attribute(lambda o: random.choice(list(Recommendation)))
    status = lazy_attribute(lambda o: random.choice(list(OrderStatus)))
    visitor = lazy_attribute(lambda o: uuid.uuid4())
    customer = SubFactory(CustomerFactory)
    payment = factory.List([factory.SubFactory(PaymentFactory) for _ in range(2)])
    billing = SubFactory(BillingFactory)
    shipping = SubFactory(ShippingFactory)
    shopping_cart = factory.List([factory.SubFactory(ProductFactory) for _ in range(2)])
    total_amount = lazy_attribute(lambda o: fake.pydecimal(left_digits=2, right_digits=4, positive=False))
    shipping_amount = lazy_attribute(lambda o: fake.pydecimal(left_digits=2, right_digits=4, positive=False))
    tax_amount = lazy_attribute(lambda o: fake.pydecimal(left_digits=2, right_digits=4, positive=False))
    currency = lazy_attribute(lambda o: fake.currency_code())
    installments = lazy_attribute(lambda o: fake.pyint(min_value=0, max_value=9999, step=5))
    ip = lazy_attribute(lambda o: fake.ipv4(network=False, address_class=None, private=None))
    first_message = lazy_attribute(lambda o: fake.date_time(tzinfo=None, end_datetime=None))
    messages_exchanged = lazy_attribute(lambda o: fake.pyint(min_value=0, max_value=9999, step=5))
    purchased_at = lazy_attribute(lambda o: fake.date_time(tzinfo=None, end_datetime=None))
    seller = SubFactory(SellerFactory)
