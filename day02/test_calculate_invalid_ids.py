import unittest
import day02.calculate_invalid_ids as this_day

class TestSomethingSomething(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.calculate_invalid_ids(this_day.sample_file), 1227775554)

    def testInputPart1(self):
        self.assertEqual(this_day.calculate_invalid_ids(this_day.input_file), 44854383294)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_ivalid_ids2(this_day.sample_file), 4174379265)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_ivalid_ids2(this_day.input_file), 55647141923)
        
