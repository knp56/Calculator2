from Calculator.Calculator import Calculator
from src.Statistics.SampleMean import sample_mean
from src.Statistics.SampleMedian import sample_median
from src.Statistics.SampleMode import sample_mode
from src.Statistics.SampleVariance import sample_variance
from src.Statistics.SampleDeviation import sample_deviation
#from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self):
        #self.data=CsvReader(filepath)
        super().__init__()


    def sample_mean(self,data):
        self.result = sample_mean(data)
        return self.result

    def sample_median(self,data):
        self.result = sample_median(data)
        return self.result

    def sample_mode(self,data):
        self.result = sample_mode(data)
        return self.result

    def sample_variance(self,data):
        self.result = sample_variance(data)
        return self.result

    def sample_deviation(self,data):
        self.result = sample_deviation(data)
        return self.result