from datetime import datetime, timedelta


class Driver:
    def __init__(self, holidays: datetime, driver_category: str, payment_per_km: int):
        self.payment_per_km = payment_per_km
        self.driver_category = driver_category
        self.holidays = holidays

    def driver_cost_per_distance(self, driving_distance):
        return self.payment_per_km * driving_distance



        