from battery.Battery import Battery


class SpindlerBattery(Battery):
    battery_lifetime = 3
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date


    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.battery_lifetime)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
