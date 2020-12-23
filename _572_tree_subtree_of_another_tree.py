# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSameTree(x: TreeNode, y: TreeNode):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and isSameTree(x.left, y.left) and isSameTree(x.right, y.right)

        if not s and not t:
            return True
        if not s or not t:
            return False
        return isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


"""
Approach #2 Using Preorder Traversal [Accepted]
=> N/A

Approach #1 By Comparison of Nodes [Accepted]

Time Complexity: O(m*n),  In worst case(skewed tree) traverse function takes O(m*n) time.
Space Complexity: O(n), The depth of the recursion tree can go upto n refers to the number of nodes in s.

"""

if __name__ == '__main__':
    demo = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)

    root2 = TreeNode(4)
    root2.left = TreeNode(1)
    root2.right = TreeNode(2)

    print(demo.isSubtree(root1, root2))
