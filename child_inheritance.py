from Ooops import Calculator # Import of Calculator class


# Inheritance

  # Use already assigned class into the new test
             # i.e., Using the parent class into child class

class childInheritance(Calculator): # Calculator class from other file is passed here to the child
    num2 = 200

    def __init__(self, a, b):
        self.digit = a
        Calculator.__init__(self, 5, 5)

    def GetAllData(self):
        print("Running child Inheritance")
        return  self.num + self.num2 + self.getdata() + self.digit


childObject = childInheritance(10, 10 )

print(childObject.GetAllData())