from Calculator.SquareRoot import square_root
from src.Statistics.SampleVariance import sample_variance

def sample_deviation(num):
    try:
        var_float = sample_variance(num)
        return round(square_root(var_float), 5)
    except ZeroDivisionError:
        print("Cannot Divide by 0")
    except ValueError:
        print("Value not found")
