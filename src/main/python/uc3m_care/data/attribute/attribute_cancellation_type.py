"""Class for the cancellation_type attribute"""
from uc3m_care.data.attribute.attribute import Attribute


# pylint: disable=too-few-public-methods
class CancellationType(Attribute):
    """Class for the cancellation_type attribute"""
    _validation_error_message = "Cancellation type is not valid"
    _validation_pattern = r"^(Temporal|Final)$"
