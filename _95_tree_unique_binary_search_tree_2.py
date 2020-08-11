# Definition for a binary tree node.
import itertools
from typing import List

m = [[] for _ in range(9)]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def newTree(x, l, r):
            t = TreeNode(x)
            t.left = l
            t.right = r
            return t

        def gen(s, e):  # e: 0~8
            return [newTree(i, l, r) for i in range(s, e + 1) for l in gen(s, i - 1) for r in gen(i + 1, e)] or [None]

        return gen(1, n) if n > 0 else []

    def help(self, start, end):
        if start > end:
            return [None]
        res = []

        for curr_root in range(start, end + 1):
            left = self.help(start, curr_root - 1)
            right = self.help(curr_root + 1, end)
            for l in left:
                for r in right:
                    root = TreeNode(curr_root)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

    def generateTreesDFS(self, n: List)-> List[TreeNode]:
        if n == 0:
            return []
        return self.help(1, n)


"""
    解題思路：
            Constraints: 0 <= n <= 8
            
            
            generateTreeDFS, 用DFS的概念下去做 / 這方法比第一個快
            Time Complexity: O(3^n) / Space Complexity: O(3^n)
            這個題目又是基於之前的96. Unique Binary Search Trees改進版的題目。之前的題目的做法是只用求出有多少組BST即可，做法是卡特蘭數。
            (可以和 894 對照看)
            
            start, curr_node, end => 是為了對應 binary search tree 的特性(左邊比較小, 右邊比較大)!!!
            
            這個題目難在構造出來。一般構造樹都需要遞歸。從1–n中任意選擇一個數當做根節點，所以其左邊的數字構成其左子樹，右邊的數字當做右子樹。
            因為要求出所有的子樹，所以當左子樹固定的時候，把所有可能的右子樹都構成，然後再變換左子樹。
            這個代碼難理解的地方在於left_nodes 和right_nodes的求法，這個一定要結合遞歸的終止條件去看，當選擇的根節點的值i比left小的時候，
            那麼其實左子樹就是空了。如果把這個理解了，那麼下面的對左右子樹的遍歷應該也不難理解。

            https://www.youtube.com/watch?v=NA-08UPnY6A
            https://blog.csdn.net/fuxuemingzhu/article/details/80778651
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = 3
    res = demo.generateTrees(input_1)
    print(res)
    output_1 = []

    # for node in res:
    #     if node:
    #         output_1.append(demo.levelOrder(node))
    #
    # for item in output_1:
    #     print(item)
