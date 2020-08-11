# Definition for a binary tree node.
import itertools
from typing import List

m = [[] for _ in range(21)]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        if len(m[N]) > 0:  # 代表之前跑過了,所以才 > 0
            return m[N]
        ans = []

        for i in range(1, N, 2):  # itertools.product => 產生多個列表和迭代器的(積)
            for l, r in itertools.product(self.allPossibleFBT(i),
                                          self.allPossibleFBT(N - i - 1)):
                root = TreeNode(0)
                root.left = l
                root.right = r
                ans.append(root)
        m[N] = ans
        # print(len(ans))
        return ans

    def allPossibleFBT2(self, N):   # 這個油allPossibleFBT4改編

        # N -= 1
        if N == 1:  # 表這個root的子結點為0
            return [TreeNode(0)]
        res = []

        for l in range(1, N, 2):
            for left in self.allPossibleFBT2(l):    # 若這裡改成l-1, 下面用 N-l 的話會錯誤！！！！(因為full binary tree 的定義！除了樹葉以外每個節點都有兩個小孩)
                # (l: 1, 3, 5) (l絕對不可能有0)
                for right in self.allPossibleFBT2(N - l - 1):   # (r: 5, 3, 1) (r也絕對不可能有0)
                    print("QQ")
                    node = TreeNode(0)
                    node.left = left
                    node.right = right
                    res.append(node)

        return res


    def allPossibleFBT4(self, N):
        N -= 1
        if N == 0:
            return [TreeNode(0)]
        res = []

        for l in range(1, N, 2):
            for left in self.allPossibleFBT4(l):
                for right in self.allPossibleFBT4(N - l):
                    node = TreeNode(0)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res


    # 這裡只是我想要試著列出結果而已,發現有困難QQ
    def levelorder(self, root: TreeNode):
        queue = []
        res = []
        queue.append(root)
        temp = TreeNode(1)

        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node.val)

            if node.left is not None:
                queue.append(node.left)
                # print(node.left.val, end=', ')

            if node.right is not None:
                queue.append(node.right)
                # print(node.right.val, end=', ')

        return res


"""
    解題思路：
            咁好難!!!!!!!!!!!!!!!!!!!!!!
            注意＊＊＊＊＊＊＊, 這題定義是要 full binary tree!!!
            full binary tree：除了樹葉以外，每個節點都有兩個小孩。 
            complete binary tree：各層節點全滿，除了最後一層，最後一層節點全部靠左。 
            perfect binary tree：各層節點全滿。 同時也是full binary tree和complete binary tree。
            
            Constraints: 1 <= N <= 20 !!!!!!!!!
            這裡用 cache 的概念去減少 Time Complexity( 因為還是有 recursion, 所以是 cache)
            
            Key observation: 1. number of nodes is always odd.
                             2. Subtrees are solutions from smaller problems.!!!
            Solution: Recursion or DP
                    tree(n):
                            for i = 1 to n, step 2:
                            root.left := trees(i)
                            root.right := trees(n-i-1)
                            
            此題目為卡特蘭函數的應用(不重要)
            
            !!!!!新觀念!!!!
            以前覺得 DP 和 cache 很像，不是都是用空間先去存以前做過的東西嗎？？？？
            NO => 好像有差異哦, => cache + recursion = DP
            https://medium.com/@rayshih771012/functional-%E8%A8%88%E7%AE%97%E6%80%9D%E7%B6%AD-recursion-%E8%88%87-dp-7ed4c28e0e32
            
            https://www.youtube.com/watch?v=noVVstnQvyY
"""

"""
    第二個方法, 可以和 95, 96 互看！！(這方法比較慢, 因為沒有用空間換取時間) (我用縮網址)
    t.ly/z15Q
    
    看這裡！！！！！！！！
    因為此題是full binary tree, 所以1個root的子結點只有兩種選擇：0個(l:0, r:0) 或2個(l:1, r:1),
    不像binary tree, 可以一個root 左邊0個 右邊1個 or 左邊0個 右邊0個
    
    full binary tree, 只能l:0 r:0 or l:1 r:1(而且 l:0 r:0 的性質只能在leaf, 所以說其實l:0 r:0 根本不能出現在判斷式!!!!!!!!!!!!)
    
    所以這就是為什麼我們這裡只有: N=1時返回 TreeNode(0)(因為full binary tree的性質)
    然而95, 96題卻有 N=0 和 N=1時的情況(表一個root 的左子結點 or 右子節點 可以為0 or 1)
    
"""

if __name__ == '__main__':
    demo = Solution()
    res_1 = demo.allPossibleFBT2(7)
    output_1 = []

    for node in res_1:
        output_1.append(demo.levelorder(node))
        # print('')

    for item in output_1:
        print(item)
