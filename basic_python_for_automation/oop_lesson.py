# classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# self keyword is mandatory for calling variable names into method
# instance and class variables should have a whole different purpose
# constructor name should be __init__
# new keyword is not required when you create objects

class Calculator:
    num = 100

    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a  # self is an object reference, it's mandatory in calling variables within a method
        self.secondNumber = b
        print("I am called automatically when object is created")

    @staticmethod
    def getData():
        print("I am now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)  # syntax to create objects in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)  # syntax to create objects in python
obj1.getData()
print(obj1.Summation())
