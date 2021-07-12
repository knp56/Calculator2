import unittest
from CsvReader.CsvReader import CsvReader, ClassFactory
#from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('/src/Tests/Data/addition.csv')
        self.csv_reader = CsvReader('/src/Tests/Data/subtraction1.csv')
        self.csv_reader = CsvReader('/src/Tests/Data/multiply.csv')
        self.csv_reader = CsvReader('/src/Tests/Data/division.csv')
        self.csv_reader = CsvReader('/src/Tests/Data/square.csv')
        self.csv_reader = CsvReader('/src/Tests/Data/square_root.csv')

if __name__ == '__main__':
    unittest.main()
