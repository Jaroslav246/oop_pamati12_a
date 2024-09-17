class Vehicle:
    name='Vehicle'

    def __init__(self,make,model,year,price):
        self=make
        self=model
        self=year
        self=price

    def display_info(self): 
        print(f"Auto nosaukums: {self.name}, Modelis: {self.model}, Gads: {self.year}, Cena {self.price} euro")
        
auto=Vehicle
auto=("Audi", "6", 2015, 10000)
auto.display_info()