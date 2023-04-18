from abc import ABC, abstractmethod
from Serviceable import Serviceable



class Car(Serviceable,ABC):
    # def __init__(self, last_service_date):
    #     self.last_service_date = last_service_date
    
    def __init__(self, engine,battery,tires):
        self.engine=engine
        self.battery=battery
        self.tires=tires

    
    def needs_service(self):
        # print("battery ",self.battery.needs_service());
        # print("engine ", self.engine.needs_service());
        # print("battery or engine ", self.engine.needs_service() or self.battery.needs_service());
        return self.engine.needs_service() or self.battery.needs_service() or self.battery.needs_service() or self.tires.needs_service()
