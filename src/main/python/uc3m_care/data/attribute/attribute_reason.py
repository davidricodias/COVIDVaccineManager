"""Class for the reason attribute"""
from uc3m_care.data.attribute.attribute import Attribute


# pylint: disable=too-few-public-methods
class Reason(Attribute):
    """Class for the cancellation_type attribute"""
    _validation_error_message = "Reason is not valid"
    _validation_pattern = r"^[a-z A-Z]{2,100}$"
