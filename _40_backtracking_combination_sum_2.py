from typing import List


class Solution:

    # DFS + recursion (沒有用到 backtracking)
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     candidates.sort()
    #     print(candidates)
    #     res = []
    #     self.dfs(candidates, target, 0, res, [])
    #     return res
    #
    # def dfs(self, nums, target, start, res, path):
    #     if target < 0:
    #         return
    #     elif target == 0:
    #         res.append(path)
    #         return
    #     for i in range(start, len(nums)):
    #         if i > start and nums[i] == nums[i - 1]:
    #             continue
    #         self.dfs(nums, target - nums[i], i + 1, res, path + [nums[i]])

    # backtracking method !
    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.helper(candidates, target, 0, res, [])
        return res

    def helper(self, candidates, target, start, res, path):
        if target < 0:
            return
        if target == 0:
            res.append(path)

        for i in range(start, len(candidates)):
            # if i > start and candidates[i] == candidates[i - 1]:    # 因為27行sort過了,所以若是有重複一定就會在隔壁, 而重複我們要忽略!!
            #     continue
            path.append(candidates[i])
            self.helper(candidates, target - candidates[i], i + 1, res, path[:])
            path.pop()


"""
    method2: 
    backtracking
    我來解釋一下 38行 for 迴圈的意思,
    在start=0的初始狀態下：
    i=0表示[?, @, #, x, x, x, x] (表示res裡面一定是由第0個位置當作開始)
    i=1表示[@, #, x, x, x, x, x] (表示res裡面一定是由第1個位置當作開始)
    So, line 39 => 避免我們重新從一樣的開頭開始(EX :[1, 1, 2])
    0位置的1 在跑完所有for迴圈後就已經可以得到1開頭的所有答案了(因為42的helper)
    若是我們又重新用第1位置的1, 這樣會有重複答案
    (不然跑一下測資 也可以知道)
    
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79343638
    
    https://www.youtube.com/watch?v=RSatA4uVBDQ
"""

if __name__ == '__main__':
    input_1 = [10, 1, 2, 7, 6, 1, 5]
    val_1 = 8
    demo = Solution()

    # print(demo.combinationSum2(input_1, val_1))
    # output_1 = demo.combinationSum3(input_1, val_1)
    # print(output_1)

    input_2 = [1, 1, 1, 1, 2]
    output_2 = demo.combinationSum3(input_2, 2)
    print(output_2)
