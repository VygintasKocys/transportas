from datetime import datetime
from transport.transport import Transport
import math


class Truck(Transport):
    def __init__(self, range_per_year: float, no: str, gasoline: str, fixed_cost: float, tech_date: datetime,
                 drives_cat: str, consumption: int, insur_date: datetime, truck_load: int, trailer: bool,
                 trailer_load: float):
        self.truck_load = truck_load
        self.trailer = trailer
        self.trailer_load = trailer_load
        super().__init__(range_per_year, no, gasoline, fixed_cost, tech_date, drives_cat, consumption, insur_date)

    def count_truck_and_trailer(self, total_load):
        truck_no = math.ceil(total_load/self.truck_load)
        for i in range(math.ceil(total_load/self.truck_load), 0, -1):
            trailer_no = math.ceil((total_load - (self.truck_load * i))/self.trailer_load)
            if trailer_no <= i:
                truck_no = i
            else:
                break
        trailer_no = math.ceil((total_load - (self.truck_load * truck_no))/self.trailer_load)
        if trailer_no < 0:
            trailer_no = 0

        print(f'reikia {trailer_no} su priekaba ir {truck_no - trailer_no} be priekabos')

    def driver_has_necessary_category(self, driver_category):
        if driver_category == self.drives_cat:
            print('Sis vairuotojas turi reikalinga kategorija vairuoti si automobili')
        else:
            print('Sis vairuotojas negali vairuoti sio automobilio')





        