# create a python class names 'Person
class Person:
# the Person class should have the following attribute: name, age, and gender 
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
# create a method called introduce that introduce Person of their name, age, and gender
    def introduce(self):
        print(f"My name is {self.name}. I am {self.age} years old and  {self.gender}")
# create an instance of Persoon class
Person1=Person("Rose", 23, "Female")
# call the introduction method
Person1.introduce()