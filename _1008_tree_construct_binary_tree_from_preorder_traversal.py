# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)

        def helper(preorder: List[int], inorder: List[int]):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            root.left = helper(preorder[1:index + 1], inorder[:index])
            root.right = helper(preorder[index + 1:], inorder[index + 1:])

            return root

        return helper(preorder, inorder)


class Solution2:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(in_left=0, in_right=len(preorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root

        inorder = sorted(preorder)
        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()


class Solution3:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lower=float('-inf'), upper=float('inf')):
            nonlocal idx
            # if all elements from preorder are used
            # then the tree is constructed
            if idx == n:
                return None

            val = preorder[idx]
            # if the current element
            # couldn't be placed here to meet BST requirements
            if val < lower or val > upper:
                return None

            # place the current element
            # and recursively construct subtrees
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(preorder)
        return helper()


"""
Approach 1: Recursion

Time Complexity: O(n^2)
Space Complexity: O(n^2)

Approach 2: Recursion , with variable

Time Complexity: O(nlogn) + O(n) = O(nlog), nlogn to sort preorder array, and O(n) to construct the binary tree
Space Complexity: O(n), the inorder traversal and the tree.

Approach 3: Advanced Recursion

Time Complexity: O(N), since we visit each node exactly once.
Space Complexity: O(N), to keep the entire tree.
"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()

    preorder = [8, 5, 1, 7, 10, 12]

    res1 = demo.bstFromPreorder(preorder)
    res2 = demo2.bstFromPreorder(preorder)
    res3 = demo3.bstFromPreorder(preorder)
