# ?write a class "calculator" capable of finding square, cube and square root of number

class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"squre of n is {self.n * self.n}")

    def cube(self):
        print(f"cube of n is {self.n * self.n * self.n} ")
    def squareroot(self):
        print(f"squareroot of n is {self.n**1/2}")

a = calculator(4)
a.square()
a.cube()
a.squareroot()