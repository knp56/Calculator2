import unittest
from CsvReader import CsvReader, ClassFactory
#from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('/src/addition.csv')
        self.csv_reader = CsvReader('/src/subtraction1.csv')
        self.csv_reader = CsvReader('/src/multiply.csv')
        self.csv_reader = CsvReader('/src/division.csv')
        self.csv_reader = CsvReader('/src/square.csv')
        self.csv_reader = CsvReader('/src/square_root.csv')

if __name__ == '__main__':
    unittest.main()
