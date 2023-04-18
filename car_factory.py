from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoPrimeTires

from car import Car


class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_arr):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_arr)

        return Car(engine, battery, tires)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_arr):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_arr)

        return Car(engine, battery, tires)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_arr):
        engine = SternmanEngine(last_service_date, warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_arr)

        tires = CarriganTires(tire_arr)

        return Car(engine, battery, tires)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_arr):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoPrimeTires(tire_arr)

        return Car(engine, battery, tires)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_arr):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoPrimeTires(tire_arr)

        return Car(engine, battery, tires)
