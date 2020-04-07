import random
import uuid

import factory
from factory import lazy_attribute, SubFactory
from faker import Faker

from konduto.api.resources.konduto_address import KondutoAddress
from konduto.api.resources.konduto_customer import KondutoCustomer
from konduto.api.resources.konduto_payment import KondutoPayment, KondutoPaymentType, KondutoPaymentStatus
from konduto.api.resources.requests.konduto_order_request import KondutoOrderRequest
from konduto.api.resources.requests.konduto_restrict_email_request import KondutoRestrictEmailRequest
from konduto.api.resources.konduto_seller import KondutoSeller
from konduto.api.resources.konduto_shopping_cart import KondutoProduct, KondutoShoppingCart

fake = Faker(locale='pt-BR')


class AddressFactory(factory.Factory):
    class Meta:
        model = KondutoAddress

    name = lazy_attribute(lambda o: fake.name())
    address1 = lazy_attribute(lambda o: fake.address())
    city = lazy_attribute(lambda o: fake.city())
    state = lazy_attribute(lambda o: fake.state_abbr())
    zip = lazy_attribute(lambda o: fake.postcode())
    country = lazy_attribute(lambda o: fake.country_code(representation='alpha-2'))


class CustomerFactory(factory.Factory):
    class Meta:
        model = KondutoCustomer

    id = lazy_attribute(lambda o: uuid.uuid4())
    name = lazy_attribute(lambda o: fake.name())
    email = lazy_attribute(lambda o: fake.email())
    dob = lazy_attribute(lambda o: fake.date(pattern='%Y-%m-%d', end_datetime=None))
    phone1 = lazy_attribute(lambda o: fake.phone_number())
    phone2 = lazy_attribute(lambda o: fake.phone_number())
    tax_id = lazy_attribute(lambda o: fake.postcode())
    created_at = lazy_attribute(lambda o: fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=40))
    new = lazy_attribute(lambda o: fake.boolean(chance_of_getting_true=50))
    vip = lazy_attribute(lambda o: fake.boolean(chance_of_getting_true=50))


class PaymentFactory(factory.Factory):
    class Meta:
        model = KondutoPayment

    type = lazy_attribute(lambda o: random.choice(list(KondutoPaymentType)))
    status = lazy_attribute(lambda o: random.choice(list(KondutoPaymentStatus)))
    bin = lazy_attribute(lambda o: fake.credit_card_number(card_type=None)[:6])
    last4 = lazy_attribute(lambda o: fake.credit_card_number(card_type=None)[-4:])
    expiration_date = lazy_attribute(lambda o: fake.credit_card_expire(start='now', end='+5y', date_format='%m%Y'))


class SellerFactory(factory.Factory):
    class Meta:
        model = KondutoSeller

    id = lazy_attribute(lambda o: str(fake.pyint(min_value=0, max_value=9999, step=1)))
    name = lazy_attribute(lambda o: fake.company())
    created_at = lazy_attribute(lambda o: fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=40))


class ProductFactory(factory.Factory):
    class Meta:
        model = KondutoProduct

    sku = lazy_attribute(lambda o: uuid.uuid4())
    product_code = lazy_attribute(lambda o: str(fake.pyint(min_value=0, max_value=9999, step=10)))
    category = lazy_attribute(lambda o: fake.pyint(min_value=0, max_value=9999, step=3))
    name = lazy_attribute(lambda o: fake.name())
    description = lazy_attribute(lambda o: fake.text())
    unit_cost = lazy_attribute(lambda o: fake.pydecimal(left_digits=2, right_digits=4, positive=True))
    quantity = lazy_attribute(lambda o: fake.pyint(min_value=0, max_value=100, step=1))
    created_at = lazy_attribute(lambda o: fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=40))


class ShoppingCartFactory(factory.Factory):
    class Meta:
        model = KondutoShoppingCart

    shopping_cart = factory.List([factory.SubFactory(ProductFactory) for _ in range(2)])


class OrderRequestFactory(factory.Factory):
    class Meta:
        model = KondutoOrderRequest

    id = lazy_attribute(lambda o: uuid.uuid4())
    visitor = lazy_attribute(lambda o: uuid.uuid4())
    customer = SubFactory(CustomerFactory)
    payment = factory.List([factory.SubFactory(PaymentFactory) for _ in range(2)])
    billing = SubFactory(AddressFactory)
    shipping = SubFactory(AddressFactory)
    shopping_cart = SubFactory(ShoppingCartFactory)
    total_amount = lazy_attribute(lambda o: fake.pydecimal(left_digits=2, right_digits=4, positive=True))
    shipping_amount = lazy_attribute(lambda o: fake.pydecimal(left_digits=2, right_digits=4, positive=True))
    tax_amount = lazy_attribute(lambda o: fake.pydecimal(left_digits=2, right_digits=4, positive=True))
    currency = lazy_attribute(lambda o: fake.currency_code())
    installments = lazy_attribute(lambda o: fake.pyint(min_value=1, max_value=12, step=1))
    ip = lazy_attribute(lambda o: fake.ipv4(network=False, address_class=None, private=None))
    first_message = lazy_attribute(lambda o: fake.date_time(tzinfo=None, end_datetime=None))
    messages_exchanged = lazy_attribute(lambda o: fake.pyint(min_value=0, max_value=9999, step=5))
    purchased_at = lazy_attribute(lambda o: fake.date_time(tzinfo=None, end_datetime=None))
    seller = SubFactory(SellerFactory)


class RestrictEmailRequestFactory(factory.Factory):
    class Meta:
        model = KondutoRestrictEmailRequest

    email_address = lazy_attribute(lambda o: fake.email())
    days_to_expire = lazy_attribute(lambda o: fake.pyint(min_value=0, max_value=9999, step=5))
