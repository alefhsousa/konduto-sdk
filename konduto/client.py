from konduto import api
from konduto.api import BaseClient


class KondutoClient(BaseClient):
    order = api.OrderClientKonduto()

    def __init__(self, private_key: str = None):
        super().__init__(private_key)
