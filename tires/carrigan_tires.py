from abc import ABC

from tires.Tires import Tires

class CarriganTires(Tires, ABC):

    def __init__(self, tire_wear):
        self.tire_wear=tire_wear

    def needs_service(self):

        for value in self.tire_wear:
            # print(value)

            if value >= 0.9 :
                return True




        return False