from src.Calculator.SquareRoot import square_root
from src.Statistics.SampleVariance import sample_variance

def sample_deviation(num):
    try:
        var_float = sample_variance(num)
        return square_root(var_float)
    except ZeroDivisionError:
        print("Cannot Divide by 0")
    except ValueError:
        print("Value not found")
