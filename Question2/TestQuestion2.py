import Question2
import unittest


########################################################################
#  UNIT TESTS
########################################################################

class CheckLinesTest(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(Question2.compare_version_strings("1.1", "1.2"), 1)

    def test_sanity_reversed(self):
        self.assertEqual(Question2.compare_version_strings("1.2", "1.1"), -1)

    def test_equal(self):
        self.assertEqual(Question2.compare_version_strings("1.1", "1.1"), 0)

    def test_many_subversions_lot_chars(self):
        self.assertEqual(Question2.compare_version_strings("1:9.0.1", "1:10.0.1"), 1)

    def test_many_subversions(self):
        self.assertEqual(Question2.compare_version_strings("1.10", "1.9.5"), -1)

    def test_many_subversions_reversed(self):
        self.assertEqual(Question2.compare_version_strings("1.10", "1.9.5"), -1)

    def test_many_subversions_reversed_smaller(self):
        self.assertEqual(Question2.compare_version_strings("1.9", "1.9.5"), 1)

    def test_first_sub_bigger(self):
        self.assertEqual(Question2.compare_version_strings("2", "1.1.1"), -1)


if __name__ == '__main__':
    unittest.main()
