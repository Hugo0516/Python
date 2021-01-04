# Definition for a Node.
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue = collections.deque()
        queue.append(root)

        while queue:
            _len = len(queue)
            for i in range(_len):
                node = queue.popleft()
                if i < _len - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


class Solution2:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = collections.deque([root])

        # Outer while loop which iterates over
        # each level
        while Q:

            # Note the size of the queue
            size = len(Q)

            # Iterate over all the nodes on the current level
            for i in range(size):

                # Pop a node from the front of the queue
                node = Q.popleft()

                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]

                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # Since the tree has now been modified, return the root node
        return root


class Solution3:

    def processChild(self, childNode, prev, leftmost):
        if childNode:

            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = childNode
            else:
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
            prev = childNode
        return prev, leftmost

    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root

        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:

            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost

            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None

            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)

                # Move onto the next node.
                curr = curr.next

        return root


"""
    *** 116 和 117 的差異在, 116 是 perfect binary tree, 而 117 不是 ***
    這議題是用 level-order traversal 的概念下去做
    116 我是寫 pre-order版本, 但是我覺得也可以寫成level-order 版本, 感覺也很直觀
    
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79560379
    
2021 / 1 / 3 updated
Approach 2: Level Order Traversal

Time Complexity: O(N)
Space Complexity: O(N)

Approach 3: Using previously established next pointers

Time Complexity: O(N)
Space Complexity: O(1)
"""
if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)

    res = demo.connect(root)
    res2 = demo2.connect(root)
    res3 = demo3.connect(root)
