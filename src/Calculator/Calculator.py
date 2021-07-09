
#from CsvReader import CsvReader
from src.Calculator.Subtraction import subtraction
from src.Calculator.Addition import addition
from src.Calculator.Multiplication import multiply
from src.Calculator.Division import divide
from src.Calculator.Square import square
from src.Calculator.SquareRoot import square_root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result = subtract(a,b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = divide(a,b)
        return self.result

    def square(self, a):
       self.result = square(a)
       return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result