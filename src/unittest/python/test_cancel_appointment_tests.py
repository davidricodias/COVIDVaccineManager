"""Tests for cancel_appointment method"""
from unittest import TestCase
import os
from freezegun import freeze_time
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from uc3m_care import JSON_FILES_PATH, JSON_FILES_RF2_PATH, JSON_FILES_FP_PATH
from uc3m_care import AppointmentsJsonStore
from uc3m_care import PatientsJsonStore
from uc3m_care import VaccinationJsonStore
from uc3m_care import CancellationJsonStore
from uc3m_care import FinalCancelledAppointmentJsonStore
from uc3m_care import TemporalCancelledAppointmentJsonStore


class TestCancelAppointment(TestCase):
    """Unit tests for cancel_appointment method in VaccineManager"""

    def setUp(self) -> None:
        # Remove store patient
        file_store = PatientsJsonStore()
        file_store.delete_json_file()
        # Remove store_date
        file_store_date = AppointmentsJsonStore()
        file_store_date.delete_json_file()
        # Remove store_vaccine
        file_store_vaccine = VaccinationJsonStore()
        file_store_vaccine.delete_json_file()
        # Remove store_cancellation
        file_store_cancellation = CancellationJsonStore()
        file_store_cancellation.delete_json_file()
        final_store = FinalCancelledAppointmentJsonStore()
        final_store.delete_json_file()
        final_store = TemporalCancelledAppointmentJsonStore()
        final_store.delete_json_file()

    @freeze_time("2022-03-08")
    def test_cancel_appointment_ok(self):
        """Test ok"""
        vaccine_date_file = JSON_FILES_RF2_PATH + "test_ok.json"
        test_file = JSON_FILES_FP_PATH + "test_ok.json"
        my_manager = VaccineManager()

        # Add a patient to the store
        my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                          "minombre tienelalongitudmaxima",
                                          "Regular", "+34123456789", "6")

        # Gets the vaccination date_signature
        value = my_manager.get_vaccine_date(vaccine_date_file, "2022-03-18")

        date_signature = my_manager.cancel_appointment(test_file)

        self.assertEqual(value, date_signature)

    @freeze_time("2022-03-08")
    def test_syntax_nok(self):
        """Loops through nok files to retrieve an exception"""

        files = [("test_dup_all.json", "JSON Decode Error - Wrong JSON Format"),
                 ("test_del_all.json", "File is not found")]
        vaccine_date_file = JSON_FILES_RF2_PATH + "test_ok.json"

        for file, error_message in files:
            with self.subTest(test=file):
                self.setUp()
                file_path = JSON_FILES_FP_PATH + file
                my_manager = VaccineManager()

                # Add a patient to the store
                my_manager.request_vaccination_id("78924cb0-075a-4099-a3ee-f3b562e805b9",
                                                  "minombre tienelalongitudmaxima",
                                                  "Regular", "+34123456789", "6")

                # Gets the vaccination date_signature
                value = my_manager.get_vaccine_date(vaccine_date_file, "2022-03-18")

                with self.assertRaises(VaccineManagementException) as c_m:
                    date_signature = my_manager.cancel_appointment(file_path)
                self.assertEqual(c_m.exception.message, error_message)
