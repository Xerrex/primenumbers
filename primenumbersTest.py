#outformat
#datatype
#no negative
#check if error is raised
#correct values
#test for one

import unittest
from primenumbers import printprimenumber

class TestPrintprimenumbers(unittest.TestCase):


    def test_if_raiseValueError(self):
        self.assertRaises(ValueError)

    def test_for_one_as_input(self):
        result = printprimenumber(1)
        expected='Input must be greater than 1'
        self.assertEqual(result,expected,'result must equal expected value')

    def test_for_negative_input(self):
        result = printprimenumber(-10)
        e_result = 'Input values should not be negatives'
        self.assertEqual(result,e_result,'the result should equal the e_result')

    def test_output_format(self):
        returnedvalue = printprimenumber(5)
        self.assertIsInstance(returnedvalue, list, "Returned value is a List")

    def test_correct_output(self):
        result = printprimenumber(5)
        e_result = [2,3,5]
        self.assertEqual(result,e_result,"the function should return the Expected result")



