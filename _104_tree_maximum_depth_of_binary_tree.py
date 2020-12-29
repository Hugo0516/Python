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


class Solution2:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


class Solution3:
    def maxDepth(self, root):

        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()

            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth


"""
    用宏觀的角度去看這個遞迴!!!! 就會覺得簡單
    t.ly/mtV0
    
    和 111, 112 比較!!

Approach 1, 2: Recursion

Time Complexity: O(N), n is the number of nodes.
Space Complexity: worst case for skew tree is O(N), for best case => balanced tree is O(LogN)

Approach 3: Iteration
Time Complexity: O(N)
Space Complexity: O(N) or O(LogN)
"""

if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(3)
    root_1.left = TreeNode(9)
    root_1.right = TreeNode(20)
    root_1.right.left = TreeNode(15)
    root_1.right.right = TreeNode(7)

    print(demo.maxDepth(root_1))
