# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None

        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        index = post.index(pre[1])
        index += 1
        root.left = self.constructFromPrePost(pre[1:1 + index], post[:index])
        root.right = self.constructFromPrePost(pre[1 + index:], post[index:-1])
        return root


class Solution2:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def make(index0, index1, N):
            if N == 0:
                return None

            root = TreeNode(pre[0])
            if N == 1:
                return root

            for L in range(N):
                if post[index1 + L - 1] == pre[index0 + 1]:
                    break

            root.left = make(index0 + 1, index1, L)
            root.right = make(index0 + L + 1, index1 + L, N - 1 - L)

            return root

        return make(0, 0, len(pre))


"""
=> Finished by myself, must witness the null index problem !!!!
=> line 18

Approach 1: Recursion

Time Complexity: O(N^2), where N is the number of nodes.
Space Complexity: O(N^2)

Approach 2:Recursion, space saving variant

Time Complexity: O(N^2)
Space Complexity: O(N), 這個比較低是因為, 我們make function傳的是數字, 並非是List,
所以存在 stack 裡面的 空間量就會比較小 !!!
"""

if __name__ == '__main__':
    demo = Solution()
    pre = [1, 2, 4, 5, 3, 6, 7]
    post = [4, 5, 2, 6, 7, 3, 1]
    res = demo.constructFromPrePost(pre, post)

    print('apple')
