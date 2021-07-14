import unittest
import numpy
from scipy import stats
#from CsvReader.CsvReader import CsvReader
#from Calculator.Calculator import Calculator
from src.Statistics.Statistics import Statistics
import random
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_sample_mean(self):
        pprint('Mean ===============================')
        mean_data= []
        with open('src/Tests/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number=int(row)
                mean_data.append(number)
        self.assertEqual(self.statistics.sample_mean(mean_data), numpy.mean(mean_data))
        pprint(mean_data)
        pprint(self.statistics.sample_mean(mean_data))
        # with open('src/Tests/Data/SampleAnswers.csv') as sample_answers:
        #     for row in sample_answers:
        #         self.assertEqual(self.Statistics.sample_mean(mean_data),))


    def test_sample_variance(self):
        pprint('Sample Variance =====================')
        variance_data=[]
        with open('src/Tests/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number=int(row)
                variance_data.append(number)
        self.assertEqual(self.statistics.sample_variance(variance_data), numpy.var(variance_data))
        pprint(variance_data)
        pprint(self.statistics.sample_variance(variance_data))

    def test_sample_deviation(self):
        pprint("Standard Deviation ===================")
        std_data= []
        with open('src/Tests/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number=int(row)
                std_data.append(number)
        self.assertEqual(self.statistics.sample_deviation(std_data), numpy.std(std_data))
        pprint(std_data)
        pprint(self.statistics.sample_deviation(std_data))

    def test_sample_median(self):
        pprint("Median ===================")
        median_data = []
        with open('src/Tests/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number = int(row)
                median_data.append(number)
        self.assertEqual(self.statistics.sample_median(median_data), numpy.median(median_data))
        pprint(median_data)
        pprint(self.statistics.sample_deviation(median_data))

    def test_sample_mode(self):
        pprint("Mode ===================")
        mode_data = []
        with open('src/Tests/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number = int(row)
                mode_data.append(number)
        self.assertEqual(self.statistics.sample_mode(mode_data), stats.mode(mode_data))
        pprint(mode_data)
        pprint(self.statistics.sample_mode(mode_data))

if __name__ == '__main__':
    unittest.main()
