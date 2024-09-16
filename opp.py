class person:
    def set(self,name,age):
        self.name = name 
        self.age = age 
    def output(self):
        print(self.name,self.age)
    def labdien(self):
        print(f'Labdien, {self.name}!')

p = person()
p.set("Peter",20)
d=person()
d.set("Dzon",24)
p.output()
p.labdien()
d.output()
d.labdien()

print("Peter",20)
int(input('Labdien, Peter!'))

