import pytest

from konduto.client import KondutoClient


class TestKondutoClient:

    def test_api_key_must_exists(self):

        with pytest.raises(Exception) as ex:
            KondutoClient()

        assert ex
        assert 'KONDUTO API KEY NOT FOUND IN YOUR ENVIRONMENT' in str(ex.value)
