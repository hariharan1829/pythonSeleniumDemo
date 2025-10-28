
#OOPS Concepts

# Inheritance: The process of acquiring the properties and behaviors (methods and attributes)
# of a parent class into a child class.
# To inherit, you pass the parent class name as an argument to the child class definition.

# Super Keyword: The 'super()' keyword is used inside a child class to call
# methods or access attributes of its parent class

# A constructor is a special method in Python (__init__) that automatically runs
# when an object of the class is created.
#
# We define it explicitly when we want to initialize class attributes
# or send argument values to the class when creating an object.
#
# 🔗 How it works:
# 1️⃣ You pass values to the constructor while creating the object.
# 2️⃣ Inside the constructor, you assign them to instance variables using self.
# 3️⃣ Those variables can then be accessed by any method in that class.

class parent:
    def greet(self):
        return "im calling parent class"

class child(parent):
    nums = 1000
    def __init__(self, title):
        self.title = title
        print(self.nums)


    def greet_child(self, num):
        par = super().greet()
        print(par)
        return f"{par} im calling child class {self.title} {num} {self.nums}"


call = child("Hariharan academy")
print(call.greet_child("100"))
print(call.greet())