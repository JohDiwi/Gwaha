class A:
    def __init__(self):
        super().__init__()
        print("Initializing A")


class B(A):
    def __init__(self):
        super().__init__()
        print("Initializing B")


class C(A):
    def __init__(self):
        super().__init__()
        print("Initializing C")


class D(C, B):
    def __init__(self):
        super().__init__()
        print("Initializing D")
d=D()

class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"Driving the {self.brand} car")

my_car = Car("Toyota")
