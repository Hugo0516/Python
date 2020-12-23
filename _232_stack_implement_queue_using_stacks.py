class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
            res = self.output.pop()
            return res
        else:
            res = self.output.pop()
            return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.output:
            return self.output[-1]
        else:
            while self.input:
                self.output.append(self.input.pop())
            return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.input and not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
Approach #1 (Two Stacks) Push - O(1) per operation, Pop - Amortized O(1) per operation.

Reference: 請看 Leetcode 講解, 為何 amortize 後為 O(1), 我其實也不是看很懂
"""

if __name__ == '__main__':
    pass
