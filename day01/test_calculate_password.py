import unittest
import day01.calculate_password as this_day

class TestCalculatePassword(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.calculate_password(this_day.sample_file), 3)

    def testInputPart1(self):
        self.assertEqual(this_day.calculate_password(this_day.input_file), 1043)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.sample_file), 0)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_something2(this_day.input_file), 0)
        
