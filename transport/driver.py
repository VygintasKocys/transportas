from datetime import datetime


class Driver:
    def __init__(self, holidays: tuple, driver_category: str, payment_per_km: int):
        self.payment_per_km = payment_per_km
        self.driver_category = driver_category
        self.holidays = holidays

    def driver_cost_per_distance(self, driving_distance):
        return self.payment_per_km * driving_distance

    def driver_on_holiday(self, today_date):
        if today_date >= self.holidays[0] <= self.holidays[1]:
            print('Vairuotojas atostogauja')
        else:
            print('Vairuotojas neatostogauja')




        