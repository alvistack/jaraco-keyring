from ..backend import KeyringBackend
from ..compat import properties


class Keyring(KeyringBackend):
    """
    Keyring that return None on every operation.

    >>> kr = Keyring()
    >>> kr.get_password('svc', 'user')
    """

    @properties.classproperty
    def priority(cls) -> float:
        return -1

    def get_password(self, service, username, password=None):
        pass

    delete_password = get_password  # type: ignore

    def set_password(self, service, username, password):
        self._validate_username(username)
