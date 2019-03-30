import Question1
import unittest


########################################################################
#  UNIT TESTS
########################################################################

class CheckLinesTest(unittest.TestCase):

    def test_equal_lines(self):
        self.assertEqual(Question1.check_overlap((2, 3), (2, 3)), True)

    def test_example_1(self):
        self.assertEqual(Question1.check_overlap((1, 5), (2, 6)), True)

    def test_example_backwards(self):
        self.assertEqual(Question1.check_overlap((5, 1), (6, 2)), True)

    def test_example_1_reversed(self):
        self.assertEqual(Question1.check_overlap((2, 6), (1, 5)), True)

    def test_example_2(self):
        self.assertEqual(Question1.check_overlap((1, 5), (6, 8)), False)

    def test_example_2_backwards(self):
        self.assertEqual(Question1.check_overlap((8, 6), (5, 1)), False)

    def test_example_2_reversed(self):
        self.assertEqual(Question1.check_overlap((6, 8), (1, 5)), False)

    def test_example_3(self):
        self.assertEqual(Question1.check_overlap((1, 5), (5, 8)), False)

    def test_example_3_reversed(self):
        self.assertEqual(Question1.check_overlap((5, 8), (1, 5)), False)

    def test_example_4(self):
        self.assertEqual(Question1.check_overlap((1, 1), (1, 1)), True)

    def test_example_5(self):
        self.assertEqual(Question1.check_overlap((3, 3), (1, 5)), True)

    def test_example_5_reversed(self):
        self.assertEqual(Question1.check_overlap((1, 5), (3, 3)), True)

    def test_example_6(self):
        self.assertEqual(Question1.check_overlap((4, 4), (4, 10)), False)

    def test_example_6_backwards(self):
        self.assertEqual(Question1.check_overlap((4, 4), (10, 4)), False)

    def test_example_6_reversed(self):
        self.assertEqual(Question1.check_overlap((4, 10), (4, 4)), False)


if __name__ == '__main__':
    unittest.main()
