"""Subclass of JsonParser for parsing inputs of cancel_appointment"""
from uc3m_care.parser.json_parser import JsonParser


class CancellationJsonParser(JsonParser):
    """Subclass of JsonParer for parsing inputs of cancel_appointment"""
    BAD_DATE_SIGNATURE_LABEL_ERROR = "Invalid date_signature"
    BAD_CANCELLATION_TYPE_LABEL_ERROR = "Invalid cancellation_type"
    BAD_REASON_LABEL_ERROR = "Invalid reason"

    DATE_SIGNATURE_KEY = "date_signature"
    CANCELLATION_TYPE_KEY = "cancellation_type"
    REASON_KEY = "reason"

    _JSON_KEYS = [DATE_SIGNATURE_KEY,
                  CANCELLATION_TYPE_KEY,
                  REASON_KEY]
    _ERROR_MESSAGES = [BAD_DATE_SIGNATURE_LABEL_ERROR,
                       BAD_CANCELLATION_TYPE_LABEL_ERROR,
                       BAD_REASON_LABEL_ERROR]
