"""Class for the attribute IsoDate"""
from datetime import date
from uc3m_care.data.attribute.attribute import Attribute
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException

#pylint: disable=too-few-public-methods
class IsoDate(Attribute):
    """Class for the attribute IsoDate"""
    _validation_pattern = r"^(20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$"
    _validation_error_message = "IsoDate invalid"

    def _validate(self, attr_value):
        """Overrides the validate method of Attribute to include the ISO validation with datetime"""
        try:
            iso_date = date.fromisoformat(attr_value)
        except ValueError as val_er:
            raise VaccineManagementException("IsoDate invalid") from val_er
        return super()._validate(iso_date.__str__())
