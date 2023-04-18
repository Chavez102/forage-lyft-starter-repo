import unittest
from datetime import datetime
import sys
from car_factory import CarFactory

from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattery

sys.path.append("..")  # Adds higher directory to python modules path.


class TestTires(unittest.TestCase):
    spindlerBattery_lifetime = SpindlerBattery.battery_lifetime

    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - self.spindlerBattery_lifetime)
        current_mileage = 0
        last_service_mileage = 0

        tires = [0.1, 0.9, 0.99, 0.2]
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - self.spindlerBattery_lifetime)
        current_mileage = 0
        last_service_mileage = 0

        tires = [0.1, 0.3, 0.4, 0.5]
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(car.needs_service())

    def test_Octoprimetires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year )
        current_mileage = 0
        last_service_mileage = 0

        tires = [0.9, 0.9, 0.9, 0.9]
        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())

    def test_Octoprimetires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year)
        current_mileage = 0
        last_service_mileage = 0

        tires = [0.0, 1, 1, .3]
        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(car.needs_service())




if __name__ == '__main__':
    print(sys.path)
    unittest.main()
