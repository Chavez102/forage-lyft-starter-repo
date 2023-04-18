from abc import ABC

from tires.Tires import Tires

class OctoPrimeTires(Tires, ABC):

    def __init__(self, tire_wear):
        self.tire_wear=tire_wear

    def needs_service(self):
        sum = 0
        for value in self.tire_wear:
            sum= sum+value

        if sum >= 3:
            return True

        return False

