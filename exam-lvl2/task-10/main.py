# Multi-level Cache System Simulation
# Objective: Design a class `CacheSystem` that simulates a two-level cache (L1 and L2). L1 cache has faster access but lower capacity than L2.
# Parameters:
# - l1_size: Integer representing the number of entries L1 cache can hold.
# - l2_size: Integer representing the number of entries L2 cache can hold.
# Returns:
# - None; methods will handle cache operations.
# Details:
# - Implement methods for `put` (to add or update data) and `get` (to retrieve data).
# - Use an LRU (Least Recently Used) policy for cache eviction when the cache is full.
# - If an item is accessed from L2, it should be moved to L1 (if there's space, otherwise evict the least recently used item from L1).


from collections import OrderedDict

class CacheSystem:
    def __init__(self, l1_size, l2_size):
        self.l1_size = l1_size
        self.l2_size = l2_size
        self.l1_cache = OrderedDict()
        self.l2_cache = OrderedDict()

    def put(self, key, value):
        if key in self.l1_cache:
            self.l1_cache.move_to_end(key)
            self.l1_cache[key] = value
        elif key in self.l2_cache:
            self.l2_cache.move_to_end(key)
            self.l2_cache[key] = value
            self._move_to_l1(key, value)
        else:
            if len(self.l1_cache) >= self.l1_size:
                self._evict_from_l1()
            self.l1_cache[key] = value

        # Ensure L1 cache size does not exceed its limit after putting a new item
        if len(self.l1_cache) > self.l1_size:
            self._move_l1_to_l2()

    def get(self, key):
        if key in self.l1_cache:
            self.l1_cache.move_to_end(key)
            return self.l1_cache[key]
        elif key in self.l2_cache:
            value = self.l2_cache.pop(key)
            self._move_to_l1(key, value)
            return value
        else:
            return None

    def _move_to_l1(self, key, value):
        if len(self.l1_cache) >= self.l1_size:
            self._evict_from_l1()
        self.l1_cache[key] = value

    def _evict_from_l1(self):
        if self.l1_cache:
            lru_key, lru_value = self.l1_cache.popitem(last=False)
            self._move_to_l2(lru_key, lru_value)

    def _move_l1_to_l2(self):
        lru_key, lru_value = self.l1_cache.popitem(last=False)
        self._move_to_l2(lru_key, lru_value)

    def _move_to_l2(self, key, value):
        if len(self.l2_cache) >= self.l2_size:
            self.l2_cache.popitem(last=False)
        self.l2_cache[key] = value
        
# Example usage:
cache = CacheSystem(2, 3)
cache.put('a', 1)
cache.put('b', 2)
print(cache.get('a') ) # Expected to access from L1
cache.put('c', 3)
cache.put('d', 4)  # Should trigger eviction in L2, moving 'c' to L1, evicting 'b'
print(cache.get('b'))  # Expected: None
print(cache.get('c'))  # Expected to move from L1, 'd' remains in L2

