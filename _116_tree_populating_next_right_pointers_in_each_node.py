import collections


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)  # pre-order!!!
        self.connect(root.right)
        return root

    # 花花版本
    def connect2(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect2(root.left)
        self.connect2(root.right)

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
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root

        # Once we reach the final level, we are done
        while leftmost.left:

            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level
            head = leftmost
            while head:

                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left

                # Progress along the list (nodes on the current level)
                head = head.next

            # Move onto the next level
            leftmost = leftmost.left

        return root


"""
    Follow up:
    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
    
    思路：
        Tree 90% => recursion
        Inordr / preorder/ postorder (這裡選preorder)
        
        善用Local view !!!!!!!!!! (隨便取一個點觀察他的特性, 然後再套用到宏觀世界)
        => cur.left.next = cur.right
        => cur.right.next = cur.next.left
        
        Time Complexity: O(n)
        Space Complexity: O(log(n))
        
        https://www.youtube.com/watch?v=YNu143ZN4qU

    https://blog.csdn.net/fuxuemingzhu/java/article/details/79559645
    
2021 / 1 / 3
*** 看到這圖, 我覺得應該要優先想到 level order traversal, 因此感覺要很自然先往 sol2 走, 而不是 sol1

Approach 2: Level order Traversal

Time Complexity: O(N), since we process each node exactly once. 
Note that processing a node in this context means popping the node from the queue and then establishing the next pointers.

Space Complexity: O(N), This is a perfect binary tree which means the last level contains N/2 nodes. 
The space complexity for breadth first traversal is the space occupied by the queue 
which is dependent upon the maximum number of nodes in particular level. So, in this case, the space complexity would be O(N). 

Approach 3: Using previously established next pointers

Time Complexity: O(N), since we process each node exactly once.
Space Complexity: O(1), since we don't make use of any additional data structure 
for traversing nodes on a particular level like the previous approach does. 
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
    root.right.left = Node(6)
    root.right.right = Node(7)

    res = demo.connect(root)
    res_2 = demo.connect2(root)
    res2 = demo2.connect(root)
    res3 = demo3.connect(root)
