class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Person created")

    def say_hello(self):
        print(f"{self.name} says Hello!")

class Student(Person):
   def __init__(self, name, age, average_grade):
      Person.__init__(self, name, age)
      print("Student created")
   def study(self):
      print(f"{self.name} studies")
   def say_hello(self):
      print(f"Student with name: {self.name} says Hello!")

class Teacher(Person):
   def teach(self):
      print(f"{self.name} teaches")





def introduce(person):
   print("Now, a person will say hello")
   person.say_hello()

people_arr=[Student("Tom", 15, 4.5), Teacher("Katy", 37), Student("Bob", 26, 4.8)]

for person in people_arr:
   introduce(person)