# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []   # 我這裡一開始寫0, 是錯的喔雞掰!!!!!!!!!!!!!!!!!!
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)

        return res[::-1]


"""
    這一題是偶自己寫粗乃ㄉ哦 嘻嘻
    
    t.ly/RUML
    網站的寫法是用 111 的寫法, 但是我覺得不用寫成那樣, 因為我們每次都只會放進真的存在的node
    不會存 null 進去, 所以我們不用有 continue 的那個判斷式的
"""


if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(3)
    root_1.left = TreeNode(9)
    root_1.right = TreeNode(20)
    root_1.right.left = TreeNode(15)
    root_1.right.right = TreeNode(17)

    print(demo.levelOrderBottom(root_1))