from Calculator.Division import divide
from Calculator.Subtraction import subtract
from Calculator.Addition import addition


def sample_median(num):
    try:
        num_values = len(num)
        list_num = [num[i] for i in range(num_values)]
        list_num.sort()
        if num_values % 2 == 0:
            median1 = list_num[int(num_values // 2)]
            median2 = list_num[int(subtract((num_values // 2), 1))]
            median_result = divide(addition(median1, median2), 2)
        else:
            median_result = list_num[int(divide(num_values, 2))]
        return median_result
    except ZeroDivisionError:
        print("Cannot Divide by 0")
    except ValueError:
        print("Value not found")