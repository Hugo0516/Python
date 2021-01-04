# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))

        return root_to_leaf


class Solution2:
    def sumNumbers(self, root: TreeNode):
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = curr_number * 10 + r.val
                # if it's a leaf, update root-to-leaf sum
                if not r.left and not r.right:
                    root_to_leaf += curr_number

                preorder(r.left, curr_number)
                preorder(r.right, curr_number)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf


class Solution22:
    def sumNumbers(self, root: TreeNode):
        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number += str(r.val)
                # if it's a leaf, update root-to-leaf sum
                if not r.left and not r.right:
                    root_to_leaf.append(curr_number)

                preorder(r.left, curr_number)
                preorder(r.right, curr_number)

        root_to_leaf = []
        preorder(root, '')
        res = 0
        for i in root_to_leaf:
            res += int(i)
        return res


class Solution3:
    def sumNumbers(self, root: TreeNode):
        root_to_leaf = curr_number = 0

        while root:
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:
                # Predecessor node is one step to the left
                # and then to the right till you can.
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val
                    predecessor.right = root
                    root = root.left
                    # Break the link predecessor.right = root
                # Once the link is broken,
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number //= 10
                    predecessor.right = None
                    root = root.right

                    # If there is no left child
            # then just go right.
            else:
                curr_number = curr_number * 10 + root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right

        return root_to_leaf


"""
*** 解題思路 ***
step 1: 看到此題型要的解果 => preorder traversal
step 2: 要用哪種方式跑 preorder? => There are 3 ways to implement preorder traversal: iterative, recursive and Morris.

Note, that Javadocs recommends to use ArrayDeque, and not Stack as a stack implementation.

Approach 1: Iterative Preorder Traversal.

Time Complexity: O(N)
Space Complexity: O(H)

Approach 2: Recursive Preorder Traversal.

Time Complexity: O(N)
Space Complexity: O(H)

Approach 22: 我自己想的, 我一開始直接想說用 string, 最後直接用 int() 把 string 轉型, 但這很浪費運算!!
Time Complexity: 估計是 O(n^2)
轉型 Reference: https://stackoverflow.com/questions/44025315/what-is-the-time-complexity-of-int1010-2
=> 所以 two based, 會花 O(N) time
=> other based, 會花 O(N^2) time


Approach 3: Morris Preorder Traversal.

Time Complexity: O(N)
Space Complexity: O(1)
"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)

    print(demo.sumNumbers(root))
    print(demo2.sumNumbers(root))
    print(demo3.sumNumbers(root))

    demo22 = Solution22()
    print(demo22.sumNumbers(root))