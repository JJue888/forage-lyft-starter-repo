import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        wear_array = [0, 0, 0.5, 1]
        tire = CarriganTire(wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        wear_array = [0, 0.5, 0.8, 0]
        tire = CarriganTire(wear_array)
        self.assertFalse(tire.needs_service())
