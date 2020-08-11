from typing import List

from numpy.core.tests.test_mem_overlap import xrange


class Solution:
    # dfs + recursion
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            if nums[index] > target:
                return
            self.dfs(nums, target - nums[i], i, res, path + [nums[i]])

    # dfs + recursion
    # def combinationSum2(self, candidatess, targett):
    #     def dfs2(candidates, target, s, curr, ans):
    #         if target == 0:
    #             ans.append(curr[:])
    #             return
    #
    #         for i in xrange(s, len(candidates)):
    #             if candidates[i] > target:
    #                 return
    #             curr.append(candidates[i])
    #             dfs2(candidates, target - candidates[i], i, curr, ans)
    #             curr.pop()
    #
    #     ans = []
    #     candidatess.sort()
    #     dfs2(candidatess, targett, 0, [], ans)
    #
    #     return ans

    # backtracking method
    def combinationSum3(self, candidates, target):
        res = []
        self.helper(candidates, target, 0, res, [])
        return res

    def helper(self, candidates, target, start, res, path):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.helper(candidates, target - candidates[i], i, res, path[:])
            path.pop()


"""
    和 113 題做比較, 27 行的問題!!!!!
    幹你娘 好難 = =
    
    在python2 的時候, xrange 比 range 還要更節省空間 (因為 xrange is iterator, range is a list)
    only be used, xrange will generate the output, however, range always store all the output
    在python3 的時候, range被改掉 只剩xrange, 但是又把xrange改名為range!!!!!
    https://blog.csdn.net/xc_zhou/article/details/80604052
    
    method 1:
    方法一：遞歸
    使用遞歸解法，這個遞歸方法是，依次遍歷每個元素，判斷其與剩餘數字的大小，如果比剩餘target小，那麼就放入到路徑path中，並且，把剩餘元素target減去當前元素。
    理解遞歸最重要的當然是遞歸函數的定義：以index為起始元素，在candidates的index元素和其之後的元素中，抽取一定的元素，能否構成和為target的路徑Path。
    
    method 3:
    其實應該要用 backtracking  方法比較好
    法ㄧ的DFS雖說也是遞歸，但是和回溯還是有區別的。因為回溯的含義，此路不通就倒著走回去，而上面的DFS是進行了全集的搜索。
    這個回溯還是很好寫的，需要一個新的函數，含義是從候選集的start位置開始向後尋找和為target的路徑。如果target等於０了就是我們終止的一個條件，即正好搜索到了一條合適的路徑。

    需要注意的是path後面的插入元素和彈出元素操作。向path中添加元素i後進行後面的搜索，搜索完之後說明i位置的所有結果都已經結束了，故向後退一步即彈出最後的元素。
    另外就是題目允許每個數字使用多次，所以for循環開始的地方是start，而往回溯函數里面傳遞的i的也是start.
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79322462
    
    method 2:
    http://zxi.mytechroad.com/blog/searching/leetcode-39-combination-sum/
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [2, 3, 6, 7]
    input_2 = [2, 3, 5]

    # print(demo.combinationSum(input_1, 7))
    # print(demo.combinationSum(input_2, 8))
    print(demo.combinationSum3(input_2, 8))
