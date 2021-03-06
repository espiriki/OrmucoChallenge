import Question2
import unittest


########################################################################
#  UNIT TESTS
########################################################################

class VersionStringTests(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(Question2.compare_version_strings("1.1", "1.1"), Question2.VERSIONS_ARE_EQUAL)

    def test_complex_equal(self):
        self.assertEqual(Question2.compare_version_strings("1:9.0.1", "1:9.0.1"), Question2.VERSIONS_ARE_EQUAL)

    def test_complex_equal_many_symbols(self):
        self.assertEqual(Question2.compare_version_strings("1;1.1,1;1;1:", "1;1;1;1;1;1,"), Question2.VERSIONS_ARE_EQUAL)

    def test_many_subversions_lot_chars(self):
        self.assertEqual(Question2.compare_version_strings("1:9.0.1", "1:10.0.1"), Question2.LHS_IS_BIGGER)

    def test_sanity(self):
        self.assertEqual(Question2.compare_version_strings("1.1", "1.2"), Question2.LHS_IS_BIGGER)

    def tests_different_lengths(self):
        self.assertEqual(Question2.compare_version_strings("1.9", "1.10.5"), Question2.LHS_IS_BIGGER)

    def test_dashes(self):
        self.assertEqual(Question2.compare_version_strings("1-9", "1-10"), Question2.LHS_IS_BIGGER)

    def test_last_one_different(self):
        self.assertEqual(Question2.compare_version_strings("1.9", "1.9.5"), Question2.LHS_IS_BIGGER)

    def test_complex_different_many_symbols(self):
        self.assertEqual(Question2.compare_version_strings("1;1;1;1;1;0", "1;1;1;1;1;1"), Question2.LHS_IS_BIGGER)

    def test_many_subversions(self):
        self.assertEqual(Question2.compare_version_strings("1.10", "1.9.5"), Question2.RHS_IS_BIGGER)

    def test_sanity_reversed(self):
        self.assertEqual(Question2.compare_version_strings("1.2", "1.1"), Question2.RHS_IS_BIGGER)

    def test_first_one_longer(self):
        self.assertEqual(Question2.compare_version_strings("1.9.5", "1.9"), Question2.RHS_IS_BIGGER)

    def test_first_bigger(self):
        self.assertEqual(Question2.compare_version_strings("2", "1.1.1"), Question2.RHS_IS_BIGGER)

    def test_first_bigger_with_zeros_fill(self):
        self.assertEqual(Question2.compare_version_strings("2.0.0.0.0.0.0.0", "1.1.1"), Question2.RHS_IS_BIGGER)


if __name__ == '__main__':
    unittest.main()
