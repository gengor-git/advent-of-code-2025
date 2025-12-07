import unittest
import day06.calculate_something as this_day

class TestCalculateMathHomework(unittest.TestCase):

    def testSamplePart1(self):
        self.assertEqual(this_day.calculate_math_homework_pt1(this_day.sample_file), 4277556)

    def testInputPart1(self):
        self.assertEqual(this_day.calculate_math_homework_pt1(this_day.input_file), 4405895212738)
        
    def testSamplePart2(self):
        self.assertEqual(this_day.calculate_math_homework_pt2(this_day.sample_file), 11)

    def testInputPart2(self):
        self.assertEqual(this_day.calculate_math_homework_pt2(this_day.input_file), 3246517)
        
