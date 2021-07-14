from src.Calculator.Square import square
from src.Calculator.Division import divide
from src.Statistics.SampleMean import sample_mean


def sample_variance(num):
    try:
        #check the sample_mean, might be reference to pop mean.py
        population_mean = sample_mean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + square(i-population_mean)
        return round(divide(x, num_values), 5)
    except ZeroDivisionError:
        print("Cannot Divide by 0")
    except ValueError:
        print("Value not found")