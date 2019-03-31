from collections import deque

MAX_CACHE_SIZE = 4
CACHE_HIT_HAPPENED = 0
CACHE_FULL_DISCARDED_LRU = 1
ADDED_TO_CACHE = 2


class MyCache:
    """In this class the MRU (most recently used) is the leftmost element of the deque
    that represents the cache memory.
    That said, the LRU (last recently used) is the rightmost element
    """

    def __init__(self):

        self.MAX_CACHE_SIZE = MAX_CACHE_SIZE
        self.cache_memory = deque()
        self.hit_count = 0

    def put_in_cache(self, element):

        # cache hit, bring it to front
        if element in self.cache_memory:
            self.cache_memory.remove(element)
            self.cache_memory.appendleft(element)
            self.hit_count = self.hit_count + 1
            return CACHE_HIT_HAPPENED

        # If its full, remove the LRU (the rightmost one) and add the current one to the cache memory
        if (len(self.cache_memory) + 1) > self.MAX_CACHE_SIZE:
            self.cache_memory.pop()
            self.cache_memory.appendleft(element)
            return CACHE_FULL_DISCARDED_LRU

        # If it's not present, append to the cache memory
        else:
            self.cache_memory.appendleft(element)
            return ADDED_TO_CACHE

    def print_hit_count(self):
        print("Hit Count = {}".format(self.hit_count))

    def print_cache_memory_content(self):
        print("Cache Memory Contains = {} ".
              format(self.return_cache_content_as_list()))

    def return_cache_content_as_list(self):
        return list(self.cache_memory)

    def return_hit_count(self):
        return self.hit_count


if __name__ == '__main__':
    pass
