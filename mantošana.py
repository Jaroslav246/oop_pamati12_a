class Table:
    def __init__(self, l, w, h):
        self.length = l 
        self.width = w
        self.height = h

    def info(self):
        print(f'Garums ir: {self.length}, platums ir: {self.width}, augstums ir: {self.height}')

class DeskTable(Table):
    def square(self):
        return self.width * self.length

t1 = Table(1.5, 1.8, 0.75)
t1.info()
t2 = DeskTable(0.8, 0.6)
print(t2.square())
t2.info()