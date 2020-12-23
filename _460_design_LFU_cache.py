from collections import defaultdict, OrderedDict


class LFUCache:
    """
    OrderedDict in python is implemented as double linked list. We could use it
    to get our least frequently used item from the keys having the same
    frequency in O(1) time.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._items = defaultdict(int)  # key: frequency.
        self._freqs = defaultdict(OrderedDict)  # frequency: {key: val}
        self._minFreq = 0  # Mininum used frequency for the keys in the cache.

    def _update_freq(self, key: int, value: int = None) -> int:
        """
        Update the _items and the _freqs with the input key, then return
        the latest value.
        """
        f = self._items[key]
        v = self._freqs[f].pop(key)  # Remove the current key.
        if value is not None:  # Update with new value if any.
            v = value

        self._freqs[f + 1][key] = v  # Add the key to the new frequency.
        self._items[key] += 1  # Update the frequency in the items.
        if self._minFreq == f and not self._freqs[f]:  # Update minimum freq.
            self._minFreq += 1

        return v

    def get(self, key: int) -> int:
        if key not in self._items:  # Not found.
            return -1

        # every operation increase the frequency of the item
        return self._update_freq(key)

    def put(self, key: int, value: int) -> None:
        if not self.capacity:  # Not able to put anything.
            return

        if key in self._items:
            # every operation increase the frequency of the item
            self._update_freq(key, value)
        else:
            if len(self._items) == self.capacity:  # Cache is full.
                # 1. Pop the least frequently used key in _freqs[mininum freq].
                # 2. Pop the same key from _items as it does not exist any more.
                self._items.pop(
                    self._freqs[self._minFreq].popitem(last=False)[0])

            # Add the new key.
            self._minFreq = 1
            self._items[key] = 1  # the frequency of new key should be 1
            self._freqs[1][key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
pass
Reference: https://leetcode.com/problems/lfu-cache/discuss/718724/Python-solution-with-OrderedDict
這解答比較像 Hua Hua 的

這一題是跟 frequency 相關, which means, every operation would make the frequency of item increase !!
"""

if __name__ == '__main__':
    demo = LFUCache(2)
    print(demo.put(1, 1))
    print(demo.put(2, 2))
    print(demo.get(1))
    print(demo.put(3, 3))
    print(demo.get(2))
    print(demo.get(3))
    print(demo.put(4, 4))
    print(demo.get(1))
    print(demo.get(3))
    print(demo.get(4))
