class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Person created")

    def say_hello(self):
      print(f"{self.name} says Hello!")

class Student(Person):
   def study(self):
      print(f"{self.name} studies")

class Teacher(Person):
   def teach(self):
      print(f"{self.name} teaches")



p1=Student("Tom", 15)
t1=Teacher("Katy", 37)
p1.say_hello()
t1.say_hello()
p1.study()
t1.teach()