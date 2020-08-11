# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return

        current_level = 0
        queue = collections.deque([(root, 1)])
        result = []
        while queue:
            node, node_level = queue.popleft()
            if node_level > current_level:
                result.append(node.val)
                current_level += 1

            if node.right:
                queue.append((node.right, node_level + 1))
            # if node.left:
            #     queue.append((node.left, node_level + 1))     # 這句多餘的？
        return result

"""
    解題思路：
            https://github.com/ryancheunggit/leetcode/blob/master/code/199_solution.py
"""

if __name__ == "__main__":
    demo = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_2 = TreeNode(5)
    right_2 = TreeNode(4)
    root.left = left
    root.right = right
    left.right = left_2
    right.right = right_2

    print(root.val, left.val, right.val, left_2.val, right_2.val)

    print(demo.rightSideView(root))
