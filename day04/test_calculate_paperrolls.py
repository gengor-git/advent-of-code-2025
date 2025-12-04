import unittest
import day04.calculate_paperrolls as this_day

class TestCalculatePaperolls(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.calculate_paperrolls_pt1(this_day.sample_file), 13)

    def testInputPart1(self):
        self.assertEqual(this_day.calculate_paperrolls_pt1(this_day.input_file), 1451)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.sample_file), 11)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.input_file), 3246517)
        
