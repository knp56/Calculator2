import unittest
import numpy
import statistics
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
        with open('src/Test/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number=int(row)
                mean_data.append(number)
        self.assertEqual(self.statistics.sample_mean(mean_data), statistics.mean(mean_data))
        pprint(mean_data)
        pprint(self.statistics.sample_mean(mean_data))
        # with open('src/Test/Data/SampleAnswers.csv') as sample_answers:
        #     for row in sample_answers:
        #         self.assertEqual(self.Statistics.sample_mean(mean_data),))


    def test_sample_variance(self):
        pprint('Sample Variance =====================')
        variance_data=[]
        with open('src/Test/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number=int(row)
                variance_data.append(number)
        self.assertAlmostEqual(self.statistics.sample_variance(variance_data), statistics.variance(variance_data))
        pprint(self.statistics.sample_variance(variance_data))

    def test_sample_deviation(self):
        pprint("Standard Deviation ===================")
        std_data= []
        with open('src/Test/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number=int(row)
                std_data.append(number)
        self.assertEqual(self.statistics.sample_deviation(std_data), statistics.stdev(std_data))
        pprint(std_data)
        pprint(self.statistics.sample_deviation(std_data))

    def test_sample_median(self):
        pprint("Median ===================")
        median_data = []
        with open('src/Test/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number = int(row)
                median_data.append(number)
        self.assertEqual(self.statistics.sample_median(median_data), statistics.median(median_data))
        pprint(median_data)
        pprint(self.statistics.sample_deviation(median_data))

    def test_sample_mode(self):
        pprint("Mode ===================")
        mode_data = []
        with open('src/Test/Data/DataSample1.csv') as text_data:
            lines = text_data.readlines()
            for row in lines:
                number = int(row)
                mode_data.append(number)
        self.assertEqual(self.statistics.sample_mode(mode_data), statistics.mode(mode_data))
        pprint(mode_data)
        pprint(self.statistics.sample_mode(mode_data))

if __name__ == '__main__':
    unittest.main()
