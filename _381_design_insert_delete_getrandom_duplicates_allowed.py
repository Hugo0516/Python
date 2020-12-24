from collections import defaultdict
from random import choice


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]:
            return False

        remove, last = self.idx[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.lst) - 1)

        self.lst.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.lst)


"""
Approach 1: ArrayList + HashMap

Time Complexity: O(N), with N being the number of operations. All of our operations are O(1),
giving N * O(1) = O(N)

Space Complexity: O(N), with N being the number of operations. 
The worst case scenario is if we get N add operations, 
in which case our ArrayList and our HashMap grow to size N.

To getRandom in O(1) and have it scale linearly with the number of copies of a value. 
The simplest solution is to store all values in a list. 
Once all values are stored, all we have to do is pick a random index.

With this in mind, the most difficult part of the problem 
becomes finding the index of the element we have to remove. 
All we have to do is have an accompanying data structure that maps the element values to their index.

"""

if __name__ == '__main__':
    pass
