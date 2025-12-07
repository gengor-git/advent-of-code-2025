import unittest
import day05.calculate_inventory as this_day

class TestCalculateInventory(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.calculate_freshness_pt1(this_day.sample_file), 3)

    def testInputPart1(self):
        self.assertEqual(this_day.calculate_freshness_pt1(this_day.input_file), 505)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_freshness_pt2(this_day.sample_file), 14)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_freshness_pt2(this_day.input_file), 344423158480189)
        
