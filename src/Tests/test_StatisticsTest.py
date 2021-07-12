import unittest
#from CsvReader.CsvReader import CsvReader
#from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics
#from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_sample_mean(self):
        mean_data= []
        with open('src/Tests/Data/DataSample1.csv') as text_data:
            for row in text_data:
                number=int(text_data.readline())
                mean_data.append(number)
        with open('src/Tests/Data/SampleAnswers.csv') as sample_answers:
            for row in sample_answers:
                self.assertEqual(self.Statistics.sample_mean(mean_data),float(row['Mean']))

    def test_sample_variance(self):
        variance_data=[]
        with open('src/Tests/Data/DataSample1.csv') as text_data:
            for row in text_data:
                number=int(text_data.readline())
                variance_data.append(number)
        with open('src/Tests/Data/SampleAnswers.csv') as sample_answers:
            for row in sample_answers:
                self.assertEqual(self.Statistics.sample_variance(variance_data),float(row['Variance']))

    def test_sample_deviation(self):
        test_data= []
        with open('src/Tests/Data/DataSample1.csv') as text_data:
            for row in text_data:
                number=int(text_data.readline())
                test_data.append(number)
        with open('src/Tests/Data/SampleAnswers.csv') as sample_answers:
            for row in sample_answers:
                self.assertEqual(self.Statistics.sample_deviation(test_data),float(row['Standard Deviation']))

if __name__ == '__main__':
    unittest.main()
