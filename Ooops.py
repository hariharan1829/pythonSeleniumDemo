#Classes and Objects
# classes are user defined blueprint or prototype
#  class will have methods, class variable, instance variable, Constructor, etc.

# when we bring a function inside a class, it is called Method
class Calculator:
    num = 100 # Class variable -- variable used inside the class

# Default Constructor -- A class always has Constructor if we don't write it there is always a Default Constructor

    def __init__(self,a,b):
        self.firstNumber = a # Instance variable
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getdata(self):
        print("Executing as method in class")
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(5, 5) # Syntax to create an object in python, we can create multiple objects
# calling instance variable and example by passing parameter

obj.getdata()
print(obj.getdata())
print(obj.num)

# outputs for the above codes
# I am called automatically when an object is created
# Executing as method in class
# Executing as method in class
# 110
# 100