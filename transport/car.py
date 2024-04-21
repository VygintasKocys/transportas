from datetime import datetime
from transport.transport import Transport


class Car(Transport):
    def __init__(self, range_per_year: float, no: str, gasoline: str, fixed_cost: float, tech_date: datetime,
                 drives_cat: str, consumption: int, insur_date: datetime):
        super().__init__(range_per_year, no, gasoline, fixed_cost, tech_date, drives_cat, consumption, insur_date)


car2 = Car(60000, "AAA555", 'Dysel', 20000, datetime(year=2005, month=12, day=30),
           'B', 8, datetime(year=2024, month=5, day=4))
