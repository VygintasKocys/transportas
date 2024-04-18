from datetime import datetime, timedelta
import math


class Transport:
    def __init__(self, range_per_year: float, no: str, gasoline: str, fixed_cost: float, tech_date: datetime,
                 drives_cat: str, consumption: int, insur_date: datetime):
        self.insur_date = insur_date
        self.consumption = consumption
        self.drives_cat = drives_cat
        self.range_per_year = range_per_year
        self.no = no
        self.gasoline = gasoline
        self.fixed_cost = fixed_cost
        self.tech_date = tech_date

    def check_tech_date_next_month(self, today_date):
        if today_date.year == self.tech_date.year and today_date.month + 1 == self.tech_date.month:
            print(f'Jusu tech aptarnavimo data {self.tech_date}')
        elif today_date.year + 1 == self.tech_date.year and today_date.month == 12 and self.tech_date.month == 1:
            print(f'Jusu tech aptarnavimo data {self.tech_date}')
        else:
            print('Kita men tech aptarnavimo daryti nereikia')

    def check_insurance_date_next_month(self, today_date):
        if today_date.year == self.insur_date.year and today_date.month + 1 == self.insur_date.month:
            print(f'Jums reikies pratesti draudima {self.insur_date}')
        elif today_date.year + 1 == self.insur_date.year and today_date.month == 12 and self.insur_date.month == 1:
            print(f'Jums reikes pratesti draudima {self.insur_date}')
        else:
            print('Kita men draudimo jums pratesti nereikia')

    def days_to_drive(self, driving_distance):
        return math.ceil(driving_distance/(self.range_per_year/365))


    def gasoline_cost(self, driving_distance: int, fuel: dict, *args): #payment_per_km):
        return fuel[self.gasoline]*driving_distance*self.consumption/100


    def fixed_cost_distance(self, driving_distance, *args):  # fuel, payment_per_km):
        return self.fixed_cost/365*self.days_to_drive(driving_distance)


    def total_cost_for_driving_distance(self,driving_distance, fuel, payment_per_km):
        return (self.gasoline_cost(driving_distance, fuel,payment_per_km)
                + self.fixed_cost_distance(driving_distance, fuel, payment_per_km) + driving_distance * payment_per_km)
















