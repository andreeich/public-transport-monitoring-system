# Import the necessary modules
import unittest
import asyncio
from typing import List, Dict

import modules.functions as f


# Test class for functions module
class TestGetDataFunctions(unittest.TestCase):
    def test_get_vehicles(self):
        vehicles = f.get_vehicles()
        self.assertTrue(isinstance(vehicles, list))

    def test_get_stops(self):
        stops = f.get_stops()
        self.assertTrue(isinstance(stops, list))

    def test_update_data(self):
        f.update_data()
        self.assertNotEqual(f.vehicles, [])
        self.assertNotEqual(f.stops, [])
