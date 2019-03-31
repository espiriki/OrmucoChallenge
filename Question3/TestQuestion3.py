import Question3
import unittest


########################################################################
#  UNIT TESTS
########################################################################

class MemoryCacheTests(unittest.TestCase):

    def setUp(self):
        self.test_cache = Question3.My_cache()

    def test_put_1_in_cache(self):
        mock_cache = [1]
        self.test_cache.put_in_cache(1)
        self.assertListEqual(self.test_cache.return_cache_content_as_list(), mock_cache)


if __name__ == '__main__':
    unittest.main()
