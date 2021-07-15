import unittest
from Test.CsvReader import CsvReader


#from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('/src/Test/Data/addition.csv')
        self.csv_reader = CsvReader('/src/Test/Data/subtraction1.csv')
        self.csv_reader = CsvReader('/src/Test/Data/multiply.csv')
        self.csv_reader = CsvReader('/src/Test/Data/division.csv')
        self.csv_reader = CsvReader('/src/Test/Data/square.csv')
        self.csv_reader = CsvReader('/src/Test/Data/square_root.csv')

if __name__ == '__main__':
    unittest.main()
