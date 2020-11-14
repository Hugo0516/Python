# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _maxPathSum(self, root):
        if not root:    # due to given "non-empty binary tree"
            return float("-inf")
        left = max(0, self._maxPathSum(root.left))
        right = max(0, self._maxPathSum(root.right))
        self.ans = max(self.ans, root.val + left + right)

        return root.val + max(left, right)

    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float("-inf")    # due to given "non-empty" binary tree
        self._maxPathSum(root)
        return int(self.ans)


"""
    這道題一開始看不太懂, 但後來知道說, 他可以經過每一個node, 但是你這node 訪問過一次之後
    就不能再訪問了~
    
    這題用的思路和技巧與 687 543 相近
     
    Reference:
    http://zxi.mytechroad.com/blog/tree/leetcode-124-binary-tree-maximum-path-sum/
    
    Time complexity O(n) / Space complexity O(h)
"""

if __name__ == '__main__':
    demo = Solution()
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(demo.maxPathSum(root))
