# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths
                else:
                    # 網路上有人說底下這一行是不好的, 因為 string is immutable,
                    # 所以每次這樣搞, 豆要從新複製, 會耗時 O(N)
                    path += '->'  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths


# 我自己寫的, 為了改進 sol1 的 str 部分
class Solution2:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths
                else:
                    # 網路上有人說底下這一行是不好的, 因為 string is immutable,
                    # 所以每次這樣搞, 豆要從新複製, 會耗時 O(N)
                    # path += '->'  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return '->'.join(i for x in paths for i in x)


class Solution3:
    def binaryTreePaths(self, root):

        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)

            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))

        return paths


"""
Approach 1: Recursion

Time Complexity: O(N), we visit each node exactly once
Space Complexity: O(N), Here we use the space for a stack call and for a paths list to store the answer.
=> Best case O(Log N)

Approach 3: Iteration:

Time Complexity: O(N)
Space Complexity: O(N)

*** 我發現 這就只是 Preorder Traversal 的改良而已 !!! ***
"""

if __name__ == '__main__':
    demo = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    ans = demo.binaryTreePaths(root)
    print(ans)

    demo2 = Solution2()
    print(demo2.binaryTreePaths(root))

    demo3 = Solution3()
    print(demo3.binaryTreePaths(root))
