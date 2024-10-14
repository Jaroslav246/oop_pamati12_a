class Table:
    def __init__(self, l, w, h):
        self.length = l 
        self.width = w
        self.height = h

    def info(self):
        print(f'Garums ir: {self.length}, platums ir: {self.width}, augstums ir: {self.height}')
class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        Table .__init__(self, l, w, h)
        self.places = p

t4 = KitchenTable(1.5, 2, 0.75, 6)