from konduto import api
from konduto.api import BaseClient


class KondutoClient(BaseClient):
    """
    The :class:`KondutoClient <KondutoClient>` object.

    Notes
    -----
        This class is the gateway to access all resource from Konduto.



    Attributes
    ----------
    private_key : str
        The key to access resources from Konduto.

    """

    order = api.OrderClientKonduto()
    restrict = api.RestrictClientKonduto()

    def __init__(self, private_key: str = None):
        super().__init__(private_key)
