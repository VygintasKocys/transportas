from datetime import datetime, timedelta
from transport.transport import Transport
from transport.car import car2
from transport.driver import Driver
from transport.duomenys import (car1, car2, truck1, bus1, today_date1, today_date2, fuel, driving_distance,
                                passenger_no, driver1)
import math


# car1.check_tech_date_next_month(datetime(year=2024, month=10, day=10))
# truck1.check_insurance_date_next_month(today_date2)
# print(car1.days_to_drive(driving_distance))
# a = car1.days_to_drive(driving_distance)
# print(car1.gasoline_cost(driving_distance,fuel, driver1.payment_per_km))
# print(a)
# print(car1.fixed_cost_distance(driving_distance, fuel, driver1.payment_per_km))
# print(bus1.total_cost_for_driving_distance(driving_distance, fuel, driver1.payment_per_km))
# print(bus1.get_busses_for_passengers(passenger_no, driving_distance, fuel, driver1.payment_per_km))
# print(bus1.total_cost_for_bus(passenger_no, driving_distance, fuel, driver1.payment_per_km))
# print(driver1.payment_per_km)
# print(driver1.driver_cost_per_distance(driving_distance))
# truck1.count_truck_and_trailer(37)

truck1.driver_has_necessary_category(driver1.driver_category)
driver1.driver_on_holiday(today_date1)
