#from Calculator.Addition import addition
from src.Calculator.Division import divide
#from Statistics.Getsample import getSample

def sample_mean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return round(divide(total,num_values),5)
    except ZeroDivisionError:
        print("Cannot Divide by 0")
    except ValueError:
        print("Value not found")
