import unittest
import day03.calculate_joltage as this_day

class TestBatteryJoltage(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.calculate_joltage_pt1(this_day.sample_file), 357)

    def testInputPart1(self):
        self.assertEqual(this_day.calculate_joltage_pt1(this_day.input_file), 17193)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_joltage_pt2(this_day.sample_file), 3121910778619)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_joltage_pt2(this_day.input_file), 171297349921310)
        
