from datetime import datetime
from transport.car import Car
from transport.bus import Bus
from transport.truck import Truck
from transport.driver import Driver

car1 = Car(40000, "BBB555", 'Benzin', 15000, datetime(year=2024, month=5, day=30),
           'B', 6, datetime(year=2024, month=5, day=4))
car2 = Car(60000, "AAA555", 'Dysel', 20000, datetime(year=2025, month=1, day=30),
           'B', 7, datetime(year=2024, month=5, day=4))
bus1 = Bus(30000, "CCC555", 'Gas', 30000, datetime(year=2025, month=1, day=18),
           'D', 12, datetime(year=2024, month=5, day=4), 30)
truck1 = Truck(35000, "DDD555", 'Dysel', 40000, datetime(year=2024, month=8, day=30),
           'E', 19, datetime(year=2025, month=1, day=4), 12, True, 5)
driver1 = Driver((datetime(year=2024, month=11, day=10), datetime(year=2024, month=11, day=15)), "E",
                1)

today_date1 = datetime(year=2024, month=4, day=18)
today_date2 = datetime(year=2024, month=12, day=14)
fuel = {'Benzin': 1.4, 'Dysel': 1.2, 'Gas': 0.9}
driving_distance = 800
passenger_no = 100
total_load = 18
