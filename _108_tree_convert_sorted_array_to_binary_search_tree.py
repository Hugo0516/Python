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


class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def to_bst(nums, start, end):
            if start > end:
                return None

            # always choose left middle node as a root
            mid = (start + end) // 2

            # preorder traversal
            node = TreeNode(nums[mid])
            node.left = TreeNode(nums, start, mid - 1)
            node.right = to_bst(nums, mid + 1, end)
            return node

        return to_bst(nums, 0, len(nums) - 1)


class Solution3:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildBST(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)

            return node

        return buildBST(0, len(nums) - 1)


"""
因為BST的中序遍歷是有序的，所以有序數組的中間的數字是根節點，序列中間節點左邊是根節點的左子樹，右邊是根節點的右子樹，以此類推。
t.ly/xEEk

Basically, the height-balanced restriction means that at each step one has to pick up the number in the middle as a root.
That works fine with arrays containing odd number of elements
but there is no predefined choice for arrays with even number of elements.

Time Complexity: O(N), since we visit each node exactly once.
Space Complexity: O(N), since O(N) to keep the output, and O(logN) for the recursion stack
------------------------------------------------------------------------

2020/12/28 sol3 updated:        *** 記住這個 ***
Reference: Hua Hua

BST: vals(root.left) <= root.val <= vals(root.right)

Height Balanced: Node(root.left) - Node(root.right) <= 1

Time Complexity: O(N), or T(n) = 2T(n/2) + O(1)
Space Complexity: O(logN)
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [-10, -3, 0, 5, 9]
    print(demo.sortedArrayToBST(input_1))
