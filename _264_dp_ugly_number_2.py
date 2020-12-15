class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1


class Solution:
    u = Ugly()

    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]


class Solution2:
    def nthUglyNumber(self, n):
        if n < 0:
            return 0

        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        # index2 代表 index2 所在的位置

        for i in range(1, n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]:
                index2 += 1
            if dp[i] == 3 * dp[index3]:
                index3 += 1
            if dp[i] == 5 * dp[index5]:
                index5 += 1

        return dp[n - 1]


"""
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

1. 1 is typically treated as an ugly number.
2. n does not exceed 1690.

Approach 1:
Time complexity : O(1) to retrieve preliminary computed ugly number, 
and about 1690×5=8450 operations for preliminary computations.

Space complexity : constant space to keep an array of 1690 ugly numbers.

Approach 2:
Time Complexity: O(n)
Space Complexity: O(n)
 *** solution2 *** 比較好,
 雖然是同樣的概念
 Reference: 負雪
"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.nthUglyNumber(10))
