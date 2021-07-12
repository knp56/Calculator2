from random import random

def getSample(data,sample_size):
    with open('.../src/Tests/Data/DataSample1.csv') as text_data:
        random_values = random.sample(data, k=sample_size)
        for num in random_values:
            text_data.write(num)
    text_data.close()
    return random_values
