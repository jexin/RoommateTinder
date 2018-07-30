import unittest
from main.py import #import the fuction
#import all things that you imported to make main.py work, like jinja and os

class TestFunction(unittest.TestCase): #rename test function to be descriptive of what we're testing
    def test_function(self): #rename test_function to be descriptive
        self.assertAlmostEqual() #add parameters
        #add more testcases
