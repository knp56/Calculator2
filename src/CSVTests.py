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


    def test_return_data_as_objects(self):
        result = self.csv_reader.return_data_as_objects('results')
        self.assertIsInstance(result,list)
        test_class = ClassFactory('results',self.csv_reader.data[0])
        for results in result:
            self.assertEqual(results.__name__,test_class.__name__)


if __name__ == '__main__':
    unittest.main()
