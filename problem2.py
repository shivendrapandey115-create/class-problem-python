# write  a class "calculator" capable of finding addition , subtraction , multipliction 
# and  square of  a number and cum of a number

class claculator:
    a = int(input("enter a first number = "))
    b = int(input("enter a second number = "))
    symbol = input ("what to do(+, *, **, ***)")
    if (symbol == "+"):
        result = a + b
        print("sum = ", result)
    elif (symbol == "*"):
        result = a * b
        print("multiplication = ", result)
    elif (symbol == "**" ):
        result = a * a
        print("square of a = ", result)
        result = b * b
        print("square of b = ", result)
    elif(symbol == "***"):
        result = a * a * a
        print("cube of a =", result)
        result  = b * b * b
        print("cube of b =", result)

c = claculator()