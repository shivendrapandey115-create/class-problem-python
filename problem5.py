# add a static method in problem 2 to get greet the user with hello


class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"squre of n is {self.n * self.n}")

    def cube(self):
        print(f"cube of n is {self.n * self.n * self.n} ")
    def squareroot(self):
        print(f"squareroot of n is {self.n**1/2}")
    @staticmethod
    def greet():
        print("hello answer is")

a = calculator(5)
a.square()
a.cube()
a.squareroot()
a.greet()