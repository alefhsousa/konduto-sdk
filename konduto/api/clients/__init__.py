from konduto.api.resources.response.error import Error
from konduto.infrastructure.either import Either, Left


def _map_to_error_if_failed(result: Either):
    return Left(Error.error_from_dict(result.value)) if result.is_left else result


class KondutoHttpClient:
    """
        The :class:`KondutoHttpClient <KondutoHttpClient>` object abstraction of http client.


        Attributes
        ----------
        client : :class:`BaseClient <BaseClient>`
            Class with attributes to acess Konduto.

    """
    def __init__(self, client=None):
        self.client = client

    def get(self, endpoint: str, **kwargs) -> Either:
        return _map_to_error_if_failed(self.client.get(endpoint, **kwargs))

    def post(self, endpoint: str, data, **kwargs) -> Either:
        return _map_to_error_if_failed(self.client.post(endpoint, data, **kwargs))

    def put(self, endpoint: str, data, **kwargs) -> Either:
        return _map_to_error_if_failed(self.client.put(endpoint, data, **kwargs))

    def delete(self, endpoint: str, **kwargs) -> Either:
        return _map_to_error_if_failed(self.client.delete(endpoint, **kwargs))
