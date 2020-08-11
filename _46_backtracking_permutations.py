from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, 0, len(nums), [], [])

    def helper(self, nums: List, degree: int, n: int, cur: List, res: List):
        if degree == n:
            res.append(cur)

        for i in range(len(nums)):
            if nums[i] in cur:
                continue
            cur.append(nums[i])
            self.helper(nums, degree + 1, n, cur[:], res)
            cur.pop()
        return res

"""
    這是自己寫出來的哦 嘻嘻
    可是我覺得還是可以 youtube 一下>,<
"""
if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 3]
    print(demo.permute(input_1))
