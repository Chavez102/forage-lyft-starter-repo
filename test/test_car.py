import unittest
from datetime import datetime
import sys
from car_factory import CarFactory

from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattery

sys.path.append("..")  # Adds higher directory to python modules path.



# from car import Car


class TestCalliope(unittest.TestCase):
    spindlerBattery_lifetime = SpindlerBattery.battery_lifetime

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - (self.spindlerBattery_lifetime + 1))
        current_mileage = 0
        last_service_mileage = 0

        tires = [0.1, 0.2, 0.2, 0.2]
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - (self.spindlerBattery_lifetime - 1))
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    spindlerBattery_lifetime = SpindlerBattery.battery_lifetime

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - (self.spindlerBattery_lifetime + 1))
        current_mileage = 0
        last_service_mileage = 0

        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())



    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year -  (self.spindlerBattery_lifetime - 1))
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    spindlerBattery_lifetime = SpindlerBattery.battery_lifetime

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()

        last_service_date = today.replace(year=today.year - (self.spindlerBattery_lifetime + 3) )
        warning_light_is_on = False

        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on,tires)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - self.spindlerBattery_lifetime)
        warning_light_is_on = False

        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on,tires)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        # car = Palindrome(last_service_date, warning_light_is_on)
        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tires)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, tires)
        self.assertFalse(car.needs_service())

#
class TestRorschach(unittest.TestCase):
    nubbin_Battery_lifetime = NubbinBattery.battery_lifetime

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - (self.nubbin_Battery_lifetime+1))
        current_mileage = 0
        last_service_mileage = 0

        # car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage,tires)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - (self.nubbin_Battery_lifetime - 1))
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tires = [0.1, 0.2, 0.2, 0.2]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        tires =[0.1 , 0.4, 0.2]
        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage,tires)

        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    nubbin_Battery_lifetime = NubbinBattery.battery_lifetime
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()

        last_service_date = today.replace(year=today.year - (self.nubbin_Battery_lifetime+1))
        current_mileage = 0
        last_service_mileage = 0

        tires = [0.1, 0.4, 0.2]
        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage,tires)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - (self.nubbin_Battery_lifetime - 1) )
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.1, 0.4, 0.2]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tires = [0.1, 0.4, 0.2]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tires = [0.1, 0.4, 0.2]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tires)

        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    print(sys.path)
    unittest.main()
