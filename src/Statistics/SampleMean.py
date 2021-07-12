#from Calculator.Addition import addition
from Calculator.Division import divide
#from Statistics.Getsample import getSample

# def sample_mean(data, sample_size):
#     total = 0
#     sample = getSample(data,sample_size)
#
#     num_values = len(sample)
#     for num in sample:
#         total = addition(total, num)
#     return divide(total.num_values)

def sample_mean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return round(divide(total,num_values),5)
    except ZeroDivisionError:
        print("Cannot Divide by 0")
    except ValueError:
        print("Value not found")
