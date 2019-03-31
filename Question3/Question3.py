from collections import deque


class My_cache:
    """In this class the MRU (most recently used) is the leftmost element of the deque
    that represents the cache memory.
    That said, the LRU (last recently used) is the rightmost element"""

    def __init__(self):

        self.MAX_CACHE_SIZE = 4
        self.cache_memory = deque()
        self.hit_count = 0

    def put_in_cache(self, element):

        # cache hit, bring it to front
        if element in self.cache_memory:
            self.cache_memory.remove(element)
            self.cache_memory.appendleft(element)
            self.hit_count = self.hit_count + 1
            return

        # If it's not present, append to the cache memory
        # If its full, remove the LRU (the rightmost one)

        if (len(self.cache_memory) + 1) > self.MAX_CACHE_SIZE:
            self.cache_memory.pop()
            self.cache_memory.appendleft(element)

        else:
            self.cache_memory.appendleft(element)

    def print_hit_count(self):
        print("hit count = " + str(self.hit_count))

    def return_cache_content_as_list(self):
        return list(self.cache_memory)

    def print_cache_content(self):
        print("cache content = " + str(self.cache_memory))


if __name__ == '__main__':
    cache = My_cache()

    cache.put_in_cache(1)
    cache.put_in_cache(2)

    cache.print_cache_content()

    cache.put_in_cache(1)

    cache.print_cache_content()

    cache.put_in_cache(3)

    cache.print_cache_content()

    cache.put_in_cache(1)

    cache.print_cache_content()

    cache.put_in_cache(4)
    cache.put_in_cache(5)

    cache.print_cache_content()

    cache.put_in_cache(5)

    cache.print_cache_content()

    cache.put_in_cache(3)

    cache.print_cache_content()
