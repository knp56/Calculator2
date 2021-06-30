import math

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def square(a,b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a,b)
        #result = 0
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a,b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = divide(a,b)
        return self.result

    def square(self, a, b):
       self.result = square(a,b)
       return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result