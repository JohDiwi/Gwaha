class Person:

    nationality = 'Ethiopian' # class attribute

    def __init__(self, name, age=70): # constructor

        self.name = age # instance attribute

        self.age = name # instance attribute

p1=Person("Mutemi", 56)
del p1.name
del Person

# inheritance in python
# the properties and Method of the parent, or base class can be inherited by the lowerclass, childclass

# create base/parent vehicle
class vehicle:
    def Vehicle_info(self):
        print("Inside parent(Vehicle) class")

# create child class, ca of vehicle class
class Car:
    def car_info(self):
        print("Inside child(car) class")

# create object of car
car=Car()

# obtain Vehicle's info using Car object
car.Vehicle_info()
car.car_info()