class LRUCache:
    def __init__(self, capacity):
        # Your implementation here
        self.lru_cache = {}
        self.current_capacity = 0
        self.max_cap = capacity
        
    def get(self, key):
        value = self.lru_cache.pop(key, -1)
        if value != -1:
            self.lru_cache[key] = value
        return value

    def put(self, key, value):
        # Insert or update. Evict LRU if over capacity.
        if key in self.lru_cache:
            self.lru_cache.pop(key)
            self.lru_cache[key] = value
        else:
            if self.current_capacity == self.max_cap:
                first_key = next(iter(self.lru_cache))
                self.lru_cache.pop(first_key)
                self.current_capacity -= 1

            self.lru_cache[key] = value
            self.current_capacity += 1

# Test
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # Expected: 1
cache.put(3, 3)
print(cache.get(2))    # Expected: -1
cache.put(4, 4)
print(cache.get(1))    # Expected: -1
print(cache.get(3))    # Expected: 3
print(cache.get(4))    # Expected: 4