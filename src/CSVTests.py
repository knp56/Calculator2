import unittest
from CsvReader import CsvReader, classfactory
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('addition.csv')

    def test_return_data_as_objects(self):
        value1 = self.csv_reader.return_data_as_objects('Value 1')
        self.assertIsInstance(value1,list)
        test_class = classfactory('Value 1',self.csv_reader.data[0])


if __name__ == '__main__':
    unittest.main()
