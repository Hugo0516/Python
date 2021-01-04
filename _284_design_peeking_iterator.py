# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._peeked_value = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # If there's not already a peeked value, get one out and store
        # it in the _peeked_value variable. We aren't told what to do if
        # the iterator is actually empty -- here I have thrown an exception
        # but in an interview you should definitely ask! This is the kind of
        # thing they expect you to ask about.
        if self._peeked_value is None:
            if not self._iterator.hasNext():
                raise StopIteration()
            self._peeked_value = self._iterator.next()

        return self._peeked_value

    def next(self):
        """
        :rtype: int
        """
        # Firstly, we need to check if we have a value already
        # stored in the _peeked_value variable. If we do, we need to
        # return it and also set _peeked_value to null so that the value
        # isn't returned again.
        if self._peeked_value is not None:
            to_return = self._peeked_value
            self._peeked_value = None
            return to_return

        if not self._iterator.hasNext():
            raise StopIteration()

        # Otherwise, we need to return a new value.
        return self._iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        # If there's a value waiting in _peeked_value, or if there are values
        # remaining in the iterator, we should return true.
        return self._peeked_value is not None or self._iterator.hasNext()


class PeekingIterator2:
    def __init__(self, iterator):
        self._next = iterator.next()
        self._iterator = iterator

    def peek(self):
        return self._next

    def next(self):
        if self._next is None:
            raise StopIteration()
        to_return = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return to_return

    def hasNext(self):
        return self._next is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class PeekingIterator3:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._next_value = None
        if self._iterator.hasNext():
            self._next_value = self._iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next_value

    def next(self):
        """
        :rtype: int
        """

        tmp = self._next_value
        if self._iterator.hasNext():
            self._next_value = self._iterator.next()
        else:
            self._next_value = None
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """

        return not self._next_value is None


"""
Approach 1: Saving Peeked Value:

Time Complexity: O(1)
Space Complexity: O(1)

Approach 2: Saving the Next Value

Time Complexity: O(1)
Space Complexity: O(1)

Approach 3: Saving the next value !!
Reference:https://www.youtube.com/watch?v=LsKkUl2r7YY

Time Complexity: O(1)
Space Complexity: O(1)

*** 記住 Approach 3 ***
"""

if __name__ == '__main__':
    pass
