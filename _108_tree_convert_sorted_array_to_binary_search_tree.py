# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        _len = len(nums)
        mid = _len // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

"""
    因為BST的中序遍歷是有序的，所以有序數組的中間的數字是根節點，序列中間節點左邊是根節點的左子樹，右邊是根節點的右子樹，以此類推。
    t.ly/xEEk
"""


if __name__ == '__main__':
    demo = Solution()
    input_1 = [-10,-3,0,5,9]
    print(demo.sortedArrayToBST(input_1))