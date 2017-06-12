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
        self.assertRaises(ValueError,printprimenumber('3'))

    def test_correct_output(self):
        test_value = printprimenumber(5)
        expected_value= 5
        self.assertEqual(test_value,expected_value,"the function should return")

    def test_for_one_as_output(self):
        values= printprimenumber(5)
        for x in values:
            self.assertEqual(x,1,"one should not be among the values")
            

    def test_output_format(self):
        returnedvalue = printprimenumber(5)
        self.assertIsInstance(returnedvalue,list,"Returned value is a List")

    def test_output_hasno_negatives(self):
         values = printprimenumber(5)
         for x in values:
             self.assertLess(x,1,"X is Less that 1")
