from datetime import datetime
from transport.transport import Transport
import math


class Bus(Transport):

    def __init__(self, range_per_year: float, no: str, gasoline: str, fixed_cost: float, tech_date: datetime,
                 drives_cat: str, consumption: int, insur_date: datetime, passengers: int):
        self.passengers = passengers
        super().__init__(range_per_year, no, gasoline, fixed_cost, tech_date, drives_cat, consumption, insur_date)

    def get_busses_for_passengers(self, passenger_no, *args):
        return math.ceil(passenger_no / self.passengers)

    def total_cost_for_bus(self, passenger_no, driving_distance, fuel, payment_per_km):
        return (self.total_cost_for_driving_distance(driving_distance, fuel, payment_per_km)
                * self.get_busses_for_passengers(passenger_no, driving_distance, fuel, payment_per_km))
