# Definition for a binary tree node.
from typing import List
import numpy as np


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def pathSum(self, root: TreeNode, sum1: int) -> List[List[int]]:
    #     res = []
    #     self.dfs(root, sum1, res, [])
    #     return res
    #
    # def dfs(self, root, target, res, path):
    #     if not root:
    #         return
    #     path += [root.val]
    #     if sum(path) == target and not root.left and not root.right:
    #         res.append(path[:])
    #         return
    #     if root.left:
    #         self.dfs(root.left, target, res, path[:])
    #     if root.right:
    #         self.dfs(root.right, target, res, path[:])
    #     path.pop(-1)

    def pathSum2(self, root, sum1):
        if not root:
            return []

        res = []
        # self.dfs2(root, sum1, res, [root.val])
        # return res
        return self.dfs2(root, sum1, res, [root.val])

    def dfs2(self, root, target, res, path):
        # if not root:
        #     return
        if sum(path) == target and not root.left and not root.right:
            res.append(path)
            # return
        if root.left:
            self.dfs2(root.left, target, res, path + [root.left.val])
        if root.right:
            self.dfs2(root.right, target, res, path + [root.right.val])

        return res

    def pathSum3(self, root, sum1):
        if not root:
            return []
        res = []
        return self.dfs3(root, sum1, res, [])

    def dfs3(self, root, target, res, path):
        path += [root.val]
        if sum(path) == target and not root.left and not root.right:
            res.append(path)
        if root.left:
            print(path, path[:])
            self.dfs3(root.left, target, res, path[:])
        if root.right:
            self.dfs3(root.right, target, res, path[:])

        return res

class Solution2:
    def __init__(self):
        self.res = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        temp = []
        self.helper(root, sum, temp)

        return self.res


    def helper(self, root: TreeNode, sum: int, temp: List):
        if root is None:
            return

        temp.append(root.val)

        if root.left is None and root.right is None and root.val == sum:
            self.res.append(temp)
        else:
            self.helper(root.left, sum-root.val, temp) or self.helper(root.right, sum-root.val, temp)


"""
    可以和 39, 40 比較
    
    第二種方法比較好, 然後我有小小改編了一下, 
    覺得比較直覺(我原本不太懂 #46 那邊return 的話 感覺很不直覺, 就是感覺會出錯 或是會直接return讓程式結束, 結果少append一個res)
    # 42 43 好像也是多餘的 = = (因為 34 35就判斷過惹) (# 48,50 因為都判斷過 node.l or node.r 為 true才會放進去, 所以應該不會再出現 node is None情形)
    
    第三種方法是, 我想說DFS 就是 pre-order traversal 阿 !!!!!!!!!!!!!!!!
    那pre-order traversal 就是先add value, 才跑 DFS(left) 和 DFS(right)阿
    所以就改寫了一下, 結果發現可以
    
    關於 #66 67, 一定得用path[:],因為[:] 是表示複製,假如今天順利運行到11, path = [5, 4, 11]
    接著程式會繼續"先"往左跑 => path = [5, 4, 11, 7] 接著往右跑 發現到尾 return res = []
    接著跳回11那個點 接著往跑右邊 path = [5, 4, 11, 7, 2] => 這樣子剛剛錯誤記下來的7 會留著, 因為一直都是用path!!!
    但是！！！！ 如果是用path[:], 那麼回到11那點時, path = [5, 4, 11] 接下來+[2] = [5, 4, 11, 2] 這樣才正確!!!!!
    
    https://blog.csdn.net/fuxuemingzhu/java/article/details/80779723
    
    
    class Solution2 才是好方法, 可以參考 112題，用一樣的絲路下去寫，然後要注意shallow copy!!
"""

if __name__ == '__main__':
    demo = Solution()
    root_1 = TreeNode(5)
    root_1.left = TreeNode(4)
    root_1.right = TreeNode(8)

    root_1.left.left = TreeNode(11)
    root_1.left.left.left = TreeNode(7)
    root_1.left.left.right = TreeNode(2)

    root_1.right.left = TreeNode(13)
    root_1.right.right = TreeNode(4)
    root_1.right.right.left = TreeNode(5)
    root_1.right.right.right = TreeNode(1)

    # output_1 = demo.pathSum(root_1, 22)
    # output_1 = demo.pathSum3(root_1, 22)
    # print(output_1)


    demo_2 = Solution2()
    output_2 = demo_2.pathSum(root_1, 22)
    print(output_2)
