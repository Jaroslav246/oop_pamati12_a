class Truck(Vehicle):
    def __init__(self, make, model, year, price, bed_length, towing_capacity):
        super().__init__(make, model, year, price)
        self.bed_length = bed_length
        self.towing_capacity = towing_capacity

truck = Truck("Ford", "F-MAX", 2013, 30000, "6162", "13 t")
truck.display_info()