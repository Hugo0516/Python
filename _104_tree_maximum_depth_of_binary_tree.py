# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


"""
    用宏觀的角度去看這個遞迴!!!! 就會覺得簡單
    t.ly/mtV0
    
    和 111, 112 比較!!
"""

if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(3)
    root_1.left = TreeNode(9)
    root_1.right = TreeNode(20)
    root_1.right.left = TreeNode(15)
    root_1.right.right = TreeNode(7)

    print(demo.maxDepth(root_1))
