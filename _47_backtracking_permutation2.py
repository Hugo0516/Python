from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        tmp = [False for i in range(len(nums))]
        return self.helper(nums, 0, len(nums), tmp, [], [])

    def helper(self, nums, degree, n, tmp, cur, res):
        if degree == n:
            if cur not in res:
                res.append(cur)

        for i in range(len(nums)):
            if tmp[i]:
                continue
            cur.append(nums[i])
            tmp[i] = True
            self.helper(nums, degree + 1, n, tmp[:], cur[:], res)
            tmp[i] = False
            cur.pop()
        return res

"""
    這題也是偶自己想粗乃ㄉ, 用這個解法也可以解46= =
    話說這解法跑測資，有點慢= =
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 3]
    output_1 = demo.permuteUnique(input_1)
    print(output_1)
