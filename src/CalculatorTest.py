import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)
    #
    # def test_add_method_calculator(self):
    #     testdata = CsvReader('/src/addition.csv').data
    #     #pprint(testdata)
    #     for row in testdata:
    #         self.assertEqual(self.calculator.add(int(row['Value 1']), row['Value 2']), int(row['Result']))
    #         self.assertEqual(self.calculator.result, int(row['Result']))
    #
    # def test_subtract_method_calculator(self):
    #     testdata = CsvReader('/src/subtraction1.csv').data
    #     #pprint(testdata)
    #     for row in testdata:
    #         self.assertEqual(self.calculator.subtract(int(row['Value 1']), row['Value 2']), int(row['Result']))
    #         self.assertEqual(self.calculator.result, int(row['Result']))
    #
    # def test_multiply_method_calculator(self):
    #     testdata = CsvReader('/src/multiply.csv').data
    #     #pprint(testdata)
    #     for row in testdata:
    #         self.assertEqual(self.calculator.multiply(int(row['Value 1']), row['Value 2']), int(row['Result']))
    #         self.assertEqual(self.calculator.result, int(row['Result']))
    #
    # def test_divide_method_calculator(self):
    #     testdata = CsvReader('/src/division.csv').data
    #     #pprint(testdata)
    #     for row in testdata:
    #         self.assertEqual(self.calculator.divide(int(row['Value 1']), row['Value 2']), int(row['Result']))
    #         self.assertEqual(self.calculator.result, int(row['Result']))

    # def test_square_method_calculator(self):
    #     testdata = CsvReader('/src/square.csv').data
    #     #pprint(testdata)
    #     for row in testdata:
    #         self.assertEqual(self.calculator.square(int(row['Value 1'])), int(row['Result ']))
    #         self.assertEqual(self.calculator.result, int(row['Result ']))
#
#     def test_square_root_method_calculator(self):
#         #self.assertEqual(2, self.calculator.square_root(4))
#         #self.assertEqual(self.calculator.result, 2)
#         testdata = CsvReader('/src/square.csv').data
#         pprint(testdata)
#         for row in testdata:
#             self.assertEqual(self.calculator.square(int(row['Value 1'])), int(row['Result ']))
#             self.assertEqual(self.calculator.result, int(row['Result ']))
#
if __name__ == '__main__':
     unittest.main()
