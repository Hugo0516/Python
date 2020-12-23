from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        self._top = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


class MyStack2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        self._top = x
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        result = self.q1.popleft()
        if self.q1:
            self._top = self.q1[0]
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


"""
Approach 1: Two queues

Time Complexity: push() to O(1), pop() to O(n)
Space Complexity:

Approach 2: Two queues

Time Complexity: pop() to O(1), push() to O(n)
Space Complexity:

Reference: https://leetcode.com/problems/implement-stack-using-queues/discuss/381976/Python-solutions
"""
