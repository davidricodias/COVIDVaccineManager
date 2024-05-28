"""File for the VaccinationCancellation class"""
from uc3m_care.data.attribute.attribute_date_signature import DateSignature
from uc3m_care.data.attribute.attribute_cancellation_type import CancellationType
from uc3m_care.data.attribute.attribute_reason import Reason

from uc3m_care.parser.cancellation_json_parser import CancellationJsonParser
from uc3m_care.storage.cancellation_json_store import CancellationJsonStore

from uc3m_care.storage.temporal_cancelled_appointments import TemporalCancelledAppointmentJsonStore
from uc3m_care.storage.final_cancelled_appointments import FinalCancelledAppointmentJsonStore


class VaccinationCancellation:
    """Class representing a cancellation event"""
    def __init__(self, date_signature, cancellation_type, reason):
        self.__date_signature = DateSignature(date_signature).value
        self.__cancellation_type = CancellationType(cancellation_type).value
        self.__reason = Reason(reason).value

    @classmethod
    def create_cancellation_from_json_file(cls, json_file):
        # Parse keys
        cancellation_parser = CancellationJsonParser(json_file)
        content = cancellation_parser.json_content

        # Creates cancellation object
        cancellation = cls(content[cancellation_parser.DATE_SIGNATURE_KEY],
                           content[cancellation_parser.CANCELLATION_TYPE_KEY],
                           content[cancellation_parser.REASON_KEY])

        return cancellation

    def log_cancelled_appointment(self, appointment):
        if self.__cancellation_type == 'Temporal':
            storage = TemporalCancelledAppointmentJsonStore()
            storage.add_item(appointment)
        elif self.__cancellation_type == 'Final':
            storage = FinalCancelledAppointmentJsonStore()
            storage.add_item(appointment)

    @property
    def date_signature(self):
        return self.__date_signature

    @property
    def cancellation_type(self):
        return self.__cancellation_type

    @property
    def reason(self):
        return self.__reason
