from random import random

def getSample(data,sample_size):
    with open('.../src/Tests/Data/DataSample1.csv') as text_data:
        random_values = random.sample(data, k=sample_size)
        for num in random_values:
            text_data.write(num)
    text_data.close()
    return random_values

#one value with seed
# def getSample(one,two):
#      random.seed(0)
#      if isinstance(one, float) and isinstance(two, float):
#          return random.randint(one,two)
#      if isinstance(one, int) and isinstance(two, int):
#         return random.randint(one,two)
#
# #one value without seed
# def getSample(one, two):
#     random.seed(0)
#     if isinstance(one, float) and isinstance(two, float):
#         return random.randint(one, two)
#     if isinstance(one, int) and isinstance(two, int):
#         return random.randint(one, two)