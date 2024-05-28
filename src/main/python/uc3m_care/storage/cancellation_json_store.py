"""Subclass of JsonStore for managing the Cancellation store"""
from uc3m_care.storage.json_store import JsonStore
from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH


class CancellationJsonStore:
    """Implements the singleton pattern"""

    # pylint: disable=invalid-name
    class __CancellationJsonStore(JsonStore):
        """Subclass of JsonStore for managing the cancellations file"""
        _FILE_PATH = JSON_FILES_PATH + "store_cancellation.json"
        _ID_FIELD = "_VaccinationCancellation__date_signature"

    instance = None

    def __new__(cls):
        if not CancellationJsonStore.instance:
            CancellationJsonStore.instance = CancellationJsonStore.__CancellationJsonStore()
        return CancellationJsonStore.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)
