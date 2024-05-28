"""Subclass of JsonStore for managing the temporal_cancelled_store_date store"""
from uc3m_care.storage.json_store import JsonStore
from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH


class TemporalCancelledAppointmentJsonStore:
    """Implements the singleton pattern"""

    # pylint: disable=invalid-name
    class __TemporalCancelledAppointmentJsonStore(JsonStore):
        """Subclass of JsonStore for managing the temporal_cancelled_store_date file"""
        _FILE_PATH = JSON_FILES_PATH + "temporal_cancelled_store_date.json"
        _ID_FIELD = "_VaccinationAppointment__date_signature"

    instance = None

    def __new__(cls):
        if not TemporalCancelledAppointmentJsonStore.instance:
            TemporalCancelledAppointmentJsonStore.instance = \
                TemporalCancelledAppointmentJsonStore.__TemporalCancelledAppointmentJsonStore()
        return TemporalCancelledAppointmentJsonStore.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)
