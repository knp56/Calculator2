from src.Calculator.Division import divide

def sample_mean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return divide(total,num_values)
    except ZeroDivisionError:
        print("Cannot Divide by 0")
    except ValueError:
        print("Value not found")
