# Import the necessary modules
import unittest

# Import the necessary modules from other files
from modules.data_layer import DataConnector
from modules.business_layer import BusinessConnector
from modules.presentation_layer import PresentationConnector


# Data layer testing class
class TestDataLayer(unittest.TestCase):
    def setUp(self) -> None:
        self.dc = DataConnector()

    def test_load_vehicles(self):
        self.assertNotEqual(self.dc._vehicles, [])

    def test_load_stops(self):
        self.assertNotEqual(DataConnector()._stops, [])


# Business layer testing class
class TestBusinessLayer(unittest.TestCase):
    def setUp(self) -> None:
        self.bc = BusinessConnector()

    def test_set_timetable(self):
        self.assertNotEqual(self.bc._timetable, {})

    def test_calc_estimated_arrival_time(self):
        location = {
            "latitude": 10.2748,
            "longitude": 9.0190
        }
        self.assertEqual(self.bc._calc_estimated_arrival_time(
            location), 84.39904214455277)


# Presentation layer testing class
class TestPresentationLayer(unittest.TestCase):
    def setUp(self) -> None:
        self.pc = PresentationConnector(True, False)

    def test_vehicles_filled(self):
        self.assertNotEqual(self.pc._vehicles, [])

    def test_stops_filled(self):
        self.assertNotEqual(self.pc._stops, [])

    def test_timetable_filled(self):
        self.assertNotEqual(self.pc._timetable, {})
