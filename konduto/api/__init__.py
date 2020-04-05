import inspect
import os
import platform

import requests
from requests import Response

from konduto import VERSION
from konduto.api.clients import KondutoHttpClient
from konduto.api.clients.v1.order import OrderClientKonduto
from konduto.api.clients.v1.restrict_list import RestrictClientKonduto
from konduto.infrastructure.either import Either, Right, Left


def _is_konduto_api_client(obj):
    return isinstance(obj, KondutoHttpClient)


def _handle_result(konduto_response: Response) -> Either:
    if konduto_response.ok:
        return Right(konduto_response.json())
    else:
        return Left(konduto_response.json()) if konduto_response.content else Left(konduto_response.reason)


class BaseClient:
    """
    The :class:`BaseClient <BaseClient>` object.

    Attributes
    ----------
    private_key : str
        The key to access resources from Konduto.

    """

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        services = inspect.getmembers(self, _is_konduto_api_client)

        for name, client in services:
            client_cls = type(client)
            client = client_cls(self)
            setattr(self, name, client)
        return self

    def __init__(self, private_key: str = None):
        self._private_key = private_key or self._find_api_key()
        self._http = requests.Session()
        self._setup_http_client()

    @property
    def key(self):
        return self._private_key

    def get(self, endpoint: str, **kwargs):
        konduto_response = self._http.get(url=endpoint, **kwargs)
        return _handle_result(konduto_response)

    def post(self, endpoint: str, data: dict, **kwargs):
        konduto_response = self._http.post(url=endpoint, data=data, **kwargs)
        return _handle_result(konduto_response)

    def put(self, endpoint: str, data: dict, **kwargs):
        konduto_response = self._http.put(url=endpoint, data=data, **kwargs)
        return _handle_result(konduto_response)

    def delete(self, endpoint: str, **kwargs):
        konduto_response = self._http.delete(url=endpoint, **kwargs)
        return _handle_result(konduto_response)

    def _setup_http_client(self):
        self._http.auth = (self.key, '')
        self._http.headers.update(self._get_heardes())

    def _get_user_agent(self) -> str:
        client = f'konduto-python-sdk/{VERSION}'
        python_version = f'Python/{platform.python_version()}'
        system_info = f'{platform.system()}/{platform.release()}'
        return f'{client} {python_version} {system_info}'

    def _get_heardes(self) -> dict:
        return {
            "User-Agent": self._get_user_agent(),
            "Content-Type": "application/json"
        }

    def _find_api_key(self) -> str:
        api_key = os.environ.get('KONDUTO_KEY')
        if not api_key:
            raise Exception('KONDUTO API KEY NOT FOUND IN YOUR ENVIRONMENT')
