import Question3
import unittest


########################################################################
#  UNIT TESTS
########################################################################

class MemoryCacheTests(unittest.TestCase):

    def setUp(self):
        self.test_cache = Question3.MyCache()

    def test_put_1_in_cache(self):
        mock_cache = [1]

        self.assertEqual(self.test_cache.put_in_cache(1), Question3.ADDED_TO_CACHE)

        # Check if the cache content is as expected
        self.assertListEqual(self.test_cache.return_cache_content_as_list(), mock_cache)

        self.assertEqual(self.test_cache.return_hit_count(), 0)

    def test_put_1_and_2_in_cache(self):
        mock_cache = [2, 1]

        self.assertEqual(self.test_cache.put_in_cache(1), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.ADDED_TO_CACHE)

        # Check if the cache content is as expected
        self.assertListEqual(self.test_cache.return_cache_content_as_list(), mock_cache)

        self.assertEqual(self.test_cache.return_hit_count(), 0)

    def test_moving_cache_hit_to_front(self):
        mock_cache = [1, 3, 2]

        self.assertEqual(self.test_cache.put_in_cache(1), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(3), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)

        # Check if the cache content is as expected
        self.assertListEqual(self.test_cache.return_cache_content_as_list(), mock_cache)

        self.assertEqual(self.test_cache.return_hit_count(), 1)

    def test_cache_limit(self):
        mock_cache = [5, 4, 3, 2]

        self.assertEqual(self.test_cache.put_in_cache(1), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(3), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(4), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(5), Question3.CACHE_FULL_DISCARDED_LRU)

        # Check if the cache content is as expected
        self.assertListEqual(self.test_cache.return_cache_content_as_list(), mock_cache)

        self.assertEqual(self.test_cache.return_hit_count(), 0)

    def test_cache_limit_and_moving_to_front(self):
        mock_cache = [1, 4, 3, 2]

        self.assertEqual(self.test_cache.put_in_cache(1), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(3), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(4), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)

        # Check if the cache content is as expected
        self.assertListEqual(self.test_cache.return_cache_content_as_list(), mock_cache)

        self.assertEqual(self.test_cache.return_hit_count(), 1)

    def test_many_cache_hits(self):
        mock_cache = [1]

        self.assertEqual(self.test_cache.put_in_cache(1), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)

        # Check if the cache content is as expected
        self.assertListEqual(self.test_cache.return_cache_content_as_list(), mock_cache)

        self.assertEqual(self.test_cache.return_hit_count(), 5)

    def test_many_cache_hits_two_values(self):
        mock_cache = [2, 1]

        self.assertEqual(self.test_cache.put_in_cache(1), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)

        # Check if the cache content is as expected
        self.assertListEqual(self.test_cache.return_cache_content_as_list(), mock_cache)

        self.assertEqual(self.test_cache.return_hit_count(), 9)

    def test_many_cache_hits_three_values(self):
        mock_cache = [3, 2, 1]

        self.assertEqual(self.test_cache.put_in_cache(1), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(1), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(2), Question3.CACHE_HIT_HAPPENED)
        self.assertEqual(self.test_cache.put_in_cache(3), Question3.ADDED_TO_CACHE)
        self.assertEqual(self.test_cache.put_in_cache(3), Question3.CACHE_HIT_HAPPENED)

        # Check if the cache content is as expected
        self.assertListEqual(self.test_cache.return_cache_content_as_list(), mock_cache)

        self.assertEqual(self.test_cache.return_hit_count(), 10)


if __name__ == '__main__':
    unittest.main()
